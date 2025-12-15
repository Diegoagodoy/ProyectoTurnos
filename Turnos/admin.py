from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Turno

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'telefono', 'email')

admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Turno)
