from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from .forms import SignupForm

# ===============================
# HOME Y SIGNUP
# ===============================
def home(request):
    return render(request, 'inicio/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login automático
            return redirect('inicio:home')
    else:
        form = SignupForm()

    return render(request, 'inicio/signup.html', {'form': form})

# ===============================
# PERFIL (EDITAR USUARIO)
# ===============================
class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # campos que podrá editar el usuario

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
