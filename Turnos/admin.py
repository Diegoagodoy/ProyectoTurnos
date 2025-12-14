from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Turno

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'telefono', 'email')  # Mostrar campos en el admin

admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Paciente, PacienteAdmin)  # Añadir el Admin personalizado
admin.site.register(Turno)
