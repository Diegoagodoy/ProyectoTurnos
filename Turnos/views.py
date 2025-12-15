from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Turno, Medico, Especialidad,Paciente
from .forms import MedicoForm, EspecialidadForm, PacienteForm

def lista_turnos(request):
    turnos = Turno.objects.select_related(
        'medico', 'paciente'
    ).order_by('fecha', 'hora')

    return render(request, 'turnos/lista_turnos.html', {
        'turnos': turnos
    })


def gestionar_medicos(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:gestionar_medicos')
    else:
        form = MedicoForm()

    medicos = Medico.objects.select_related('especialidad').order_by('apellido')

    return render(request, 'turnos/gestionar_medicos.html', {
        'form': form,
        'medicos': medicos
    })

def gestionar_especialidades(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:gestionar_especialidades')
    else:
        form = EspecialidadForm()

    especialidades = Especialidad.objects.all().order_by('nombre')

    return render(request, 'turnos/gestionar_especialidades.html', {
        'form': form,
        'especialidades': especialidades
    })

def gestionar_pacientes(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:gestionar_pacientes')
    else:
        form = PacienteForm()

    pacientes = Paciente.objects.order_by('apellido', 'nombre')

    return render(request, 'turnos/gestionar_pacientes.html', {
        'form': form,
        'pacientes': pacientes
    })

def crear_turno(request):
    return HttpResponse("Formulario de turnos (en construcción)")
