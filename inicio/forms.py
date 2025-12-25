from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        label="Apellido",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class NuestraClinicaForm(forms.Form):
    titulo = forms.CharField(max_length=200, initial="Nuestra Clínica")
    descripcion = forms.CharField(widget=forms.Textarea, initial="Bienvenido a nuestra clínica, un espacio dedicado a brindar atención médica de calidad.")
    imagen = forms.CharField(max_length=200, initial='inicio/img/clinica.jpg')  # ruta al static
