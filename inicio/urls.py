from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import home, signup, perfil  # <-- agregamos perfil

app_name = 'inicio'

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='inicio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('inicio:home')), name='logout'),
    path('signup/', signup, name='signup'),

    # Perfil de usuario
    path('perfil/', perfil, name='perfil'),

    # Cambio de contraseña
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='inicio/password_change.html',
            success_url=reverse_lazy('inicio:perfil')
        ),
        name='password_change'
    ),
]
