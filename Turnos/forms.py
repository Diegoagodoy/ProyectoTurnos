from django import forms
from .models import Medico, Especialidad, Paciente

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'especialidad']


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['apellido','nombre', 'dni', 'telefono', 'email']