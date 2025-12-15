from django.shortcuts import render , redirect
from .models import Turno, Medico, Especialidad,Paciente
from .forms import MedicoForm, EspecialidadForm, PacienteForm, TurnoForm


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
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_turnos')
    else:
        form = TurnoForm()

    return render(request, 'turnos/crear_turno.html', {'form': form})

from django.shortcuts import render
from .models import Turno, Medico, Paciente, Especialidad

def lista_turnos(request):
    turnos = Turno.objects.select_related('medico', 'paciente', 'medico__especialidad').all().order_by('fecha', 'hora')

    # Filtros
    especialidad_id = request.GET.get('especialidad')
    medico_id = request.GET.get('medico')
    paciente_id = request.GET.get('paciente')
    fecha = request.GET.get('fecha')
    estado = request.GET.get('estado')

    if especialidad_id:
        turnos = turnos.filter(medico__especialidad_id=especialidad_id)
    if medico_id:
        turnos = turnos.filter(medico_id=medico_id)
    if paciente_id:
        turnos = turnos.filter(paciente_id=paciente_id)
    if fecha:
        turnos = turnos.filter(fecha=fecha)
    if estado:
        turnos = turnos.filter(estado=estado)

    especialidades = Especialidad.objects.all()
    medicos = Medico.objects.all()
    pacientes = Paciente.objects.all()

    return render(request, 'turnos/lista_turnos.html', {
        'turnos': turnos,
        'especialidades': especialidades,
        'medicos': medicos,
        'pacientes': pacientes,
        'filtros': {
            'especialidad': especialidad_id,
            'medico': medico_id,
            'paciente': paciente_id,
            'fecha': fecha,
            'estado': estado,
        }
    })
