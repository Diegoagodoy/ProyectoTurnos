from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from .forms import SignupForm, NuestraClinicaForm


def home(request):
    return render(request, 'inicio/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('inicio:home')
    else:
        form = SignupForm()

    return render(request, 'inicio/signup.html', {'form': form})


class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('inicio:perfil')
    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'inicio/perfil.html', {'form': form})

def nuestra_clinica(request):
    titulo = request.session.get('titulo_clinica', 'Nuestra Clínica')
    descripcion = request.session.get('descripcion_clinica', 'Bienvenido a nuestra clínica, un espacio dedicado a brindar atención médica de calidad.')
    imagen = request.session.get('imagen_clinica', 'inicio/img/clinica.jpg')
    
    return render(request, 'inicio/nuestra_clinica.html', {
        'titulo': titulo,
        'descripcion': descripcion,
        'imagen': imagen
    })


@login_required
def editar_clinica(request):
    if request.method == 'POST':
        form = NuestraClinicaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            imagen = form.cleaned_data['imagen']
            request.session['titulo_clinica'] = titulo
            request.session['descripcion_clinica'] = descripcion
            request.session['imagen_clinica'] = imagen
            return redirect('inicio:nuestra_clinica')
    else:
        initial_data = {
            'titulo': request.session.get('titulo_clinica', 'Nuestra Clínica'),
            'descripcion': request.session.get('descripcion_clinica', 'Bienvenido a nuestra clínica, un espacio dedicado a brindar atención médica de calidad.'),
            'imagen': request.session.get('imagen_clinica', 'inicio/img/clinica.jpg')
        }
        form = NuestraClinicaForm(initial=initial_data)
    
    return render(request, 'inicio/editar_clinica.html', {'form': form})