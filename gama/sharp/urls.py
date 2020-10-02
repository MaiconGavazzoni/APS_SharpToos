from django.urls import path
from .views import list, itens_list, create_list, list_update, list_delete, categoria_print, delete


app_name = 'sharp'

urlpatterns = [
    path('lista/', list, name='list'),
    path('lista/<int:pk>', itens_list, name='itens_list'),#lista dos itens
    path('lista/create', create_list, name='create_list'),#cria novo item
    path('lista/<int:pk>/update', list_update, name='list_update'),
    path('lista/<int:pk>/delete', list_delete, name='list_delete'),
    path('lista/<int:pk>/deletar', delete, name='delete'),
    path('lista/print.pdf', categoria_print, name='categoria_print'),
    path('lista/<int:pk>/Lista.pdf', categoria_print, name='categoria_print_one'),

]