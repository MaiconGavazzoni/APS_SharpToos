from django.forms import ModelForm
from django import forms
from .models import Sharpen, ListSharpen
from django.conf import settings
from gama.core.mail import send_mail_template

class CriaListaForm(ModelForm):
    class Meta:
        model= Sharpen
        fields = ['name_sharpen', 'author']

class InsertItem(ModelForm):
    class Meta:
        model = ListSharpen
        fields = ['tools', 'quantity', 'sharpen']

class UpdateItem(ModelForm):
    class Meta:
        model = ListSharpen
        fields = ['tools', 'quantity']

class DeleteItem(ModelForm):
    class Meta:
        model = ListSharpen
        fields = ['tools']

class ContactCourse(forms.Form):

    name = forms.CharField(label='Seu Nome', max_length=30)
    email = forms.EmailField(label='Seu e-mail')
    message = forms.CharField(
    label='Mensagem', widget=forms.Textarea (attrs={ 'cols' :  '40' ,  'rows' :  '2' })

    )

    def send_mail(self, pk):
        itens = ListSharpen.objects.filter(sharpen=pk)
        nome = Sharpen.objects.get(id=pk)
        subject ='Lista de Afiação [%s]' % nome.name_sharpen #passa o slug com subject pois facita saber de qual curso se trata
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        context['item'] = itens
        template_name = 'sharp/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )




