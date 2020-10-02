from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Tools, Sharpen, ListSharpen
from django.contrib import messages
#from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .form import CriaListaForm, InsertItem, UpdateItem, DeleteItem, ContactCourse
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse, FileResponse
from django.template.loader import render_to_string
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

# Create your views here.


@login_required
def list(request):
    form = CriaListaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CriaListaForm()

    lista = Sharpen.objects.all()
    template_name = 'sharp/list.html'
    context = {
        'form': form,
        'lista': lista
    }
    return render(request, template_name, context)
"""
@login_required
def itensList(request, pk):
    form = ListSharpenForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListSharpenForm()

    query = ListSharpen.objects.filter(sharpen=pk)
    item = query.all()
    template_name = 'sharp/itensList.html'
    context = {
        'form': form,
        'item': item
    }
    return render(request, template_name, context)
"""
"""
def itensList(request, pk):
    afia = Sharpen.objects.get(pk=pk)
    ListInlineFormSet = inlineformset_factory(Sharpen, ListSharpen, fields=('tools','quantity',), max_num=1)
    ListInlineFormSet()
    if request.method == "POST":
        formset = ListInlineFormSet(request.POST, request.FILES, instance=afia)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:

            return HttpResponseRedirect(reverse('sharp:itensList', args=(afia.pk,)))

    else:
        formset = ListInlineFormSet()

    query = ListSharpen.objects.filter(sharpen=pk)
    item = query.all()
    template_name = 'sharp/itensList.html'
    context = {
        'form': formset,
        'item': item
    }
    return render(request, template_name, context)

def alterList(request, pk):
    item = ListSharpen.objects.get(pk=pk)
    ListformSet = formset_factory(Sharpen, ListSharpen, fields=('quantity',), max_num=1)
    ListformSet()
    if request.method == "POST":
        formset = ListformSet(request.POST, request.FILES, instance=item)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:

            return HttpResponseRedirect(reverse('sharp:itensList', args=(item.sharpen,)))

    else:
        formset = ListformSet()

    query = ListSharpen.objects.filter(item.sharpen)
    itens = query.all()
    template_name = 'sharp/itensList.html'
    context = {
        'form': formset,
        'item': itens
    }
    return render(request, template_name, context)
#original funciona    
def itens_list(request, pk):
    itens = ListSharpen.objects.filter(sharpen=pk)
    pk = pk
    template_name = 'sharp/CRUD_itens_list.html'
    context = {
        'item' : itens,
        'pk':pk,
    }
    return render(request,template_name, context)    
#    
    
def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)    
    
    
    
    
    
    
"""
def delete(request, pk):
    item = Sharpen.objects.get(pk=pk)
    if item.delete()==True:
        messages.success(request, 'A lista  foi deletada com sucesso')
        return redirect('sharp:list')
    return HttpResponseRedirect(reverse('sharp:list'))




def itens_list(request, pk):
    itens = ListSharpen.objects.filter(sharpen=pk)
    pk = pk
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(pk)
            form = ContactCourse()
    else:
        form = ContactCourse()
    template_name = 'sharp/CRUD_itens_list.html'
    context['form'] = form
    context['item'] = itens
    context['pk'] = pk
    return render(request,template_name, context)


def save_list_form(request, form, template_name, pk):
    itens = get_object_or_404(ListSharpen, pk=pk)
    id = itens.sharpen
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            itens = ListSharpen.objects.filter(sharpen=id)
            data['html_book_list'] = render_to_string('sharp/partial_list.html', {
                'item': itens
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def create_list(request):
    if request.method == 'POST':
        form = InsertItem(request.POST,)

    else:

        form = InsertItem()
    return save_create_form(request, form, 'sharp/partial_create_item.html')

def save_create_form(request, form, template_name):

    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True

            data['html_book_list'] = render_to_string('sharp/partial_list.html', {

            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)





def list_update(request, pk):
    list = get_object_or_404(ListSharpen, pk=pk)
    pk = pk
    if request.method == 'POST':
        form = UpdateItem(request.POST, instance=list)
    else:
        form = UpdateItem(instance=list)
    return save_list_form(request, form, 'sharp/partial_list_update.html', pk)

def list_delete(request, pk):
    itens = get_object_or_404(ListSharpen, pk=pk)
    id = itens.sharpen
    data = dict()
    if request.method == 'POST':
        itens.delete()
        data['form_is_valid'] = True
        itens = ListSharpen.objects.filter(sharpen=id)
        data['html_book_list'] = render_to_string('sharp/partial_list.html', {
            'item': itens
        })
    else:
        context = {'item': itens}
        data['html_form'] = render_to_string('sharp/partial_list_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)



"""
def list_delete(request, pk):
    itens = get_object_or_404(ListSharpen, pk=pk)
    data = dict()
    if request.method == 'POST':
        form = DeleteItem(request.POST, instance=itens)
        form.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        itens = ListSharpen.objects.filter(sharpen=7)
        data['html_book_list'] = render_to_string('sharp/partial_list.html', {
                'item': itens
        })
    else:
        context = {'item': itens}
        data['html_form'] = render_to_string('sharp/partial_list_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
"""
"""
#View PDF

class ReportePersonasPDF(View):
    def cabecera(self, pdf):
        # Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+ 'assets/img/download.png'
        # Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 212, 238, 120, 90, preserveAspectRatio=True)

    def get(self, request, *args, **kwargs):
        # Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='sharp/pdf')
        # La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        # Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        # Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        # Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
"""

#Gerador de PDF
def categoria_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='sharp/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    categorias = []
    styles = getSampleStyleSheet()
    header = Paragraph("Lista de Afiação " , styles['Heading1'])
    categorias.append(header)
    headings = ('Id', 'Name', 'Autor', 'Created')
    if not pk:
        todascategorias = [(p.id, p.name_sharpen, p.author, p.created)
                           for p in Sharpen.objects.all().order_by('pk')]
    else:
        todascategorias = [(p.tools.stock_code, p.sharpen.author, p.tools, p.quantity)
                           for p in ListSharpen.objects.filter(sharpen=pk)]
    t = Table([headings] + todascategorias)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    categorias.append(t)
    doc.build(categorias)
    response.write(buff.getvalue())
    buff.close()
    return response

#envio de Email
def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)