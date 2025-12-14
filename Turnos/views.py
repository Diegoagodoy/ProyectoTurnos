from django.shortcuts import render
from .models import Turno

def lista_turnos(request):
    turnos = Turno.objects.select_related(
        'medico', 'paciente'
    ).order_by('fecha', 'hora')

    return render(request, 'turnos/lista_turnos.html', {
        'turnos': turnos
    })

