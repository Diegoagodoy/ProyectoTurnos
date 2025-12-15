from django import forms
from .models import Medico, Especialidad, Paciente, Turno

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


class TurnoForm(forms.ModelForm):
    especialidad = forms.ModelChoiceField(
        queryset=Especialidad.objects.all(),
        required=True,
        label="Especialidad"
    )

    class Meta:
        model = Turno
        fields = ['especialidad', 'medico', 'paciente', 'fecha', 'hora', 'estado']

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medico'].queryset = Medico.objects.all()  
