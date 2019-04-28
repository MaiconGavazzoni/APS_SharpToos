from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, dashboard, edit, edit_password, password_reset, password_reset_confirm

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view
        (template_name='accounts/entrar.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view
        (template_name='core/index.html'), name='logout'),
    path('cadastre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('confirmar-nova-senha/<str:key>', password_reset_confirm, name='password_reset_confirm'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password, name='edit_password'),
]