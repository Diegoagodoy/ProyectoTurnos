from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Turno, Medico, Especialidad, Paciente
from .forms import MedicoForm, EspecialidadForm, PacienteForm, TurnoForm


@login_required
def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_turnos')
    else:
        form = TurnoForm()

    return render(request, 'turnos/crear_turno.html', {'form': form})


def superuser_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper


@superuser_required
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


@superuser_required
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


@superuser_required
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


class TurnoListView(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'turnos/lista_turnos.html'
    context_object_name = 'turnos'

    def get_queryset(self):
        qs = Turno.objects.select_related('medico', 'paciente', 'medico__especialidad').all().order_by('fecha', 'hora')

        especialidad_id = self.request.GET.get('especialidad')
        medico_id = self.request.GET.get('medico')
        paciente_id = self.request.GET.get('paciente')
        fecha = self.request.GET.get('fecha')
        estado = self.request.GET.get('estado')

        if especialidad_id:
            qs = qs.filter(medico__especialidad_id=especialidad_id)
        if medico_id:
            qs = qs.filter(medico_id=medico_id)
        if paciente_id:
            qs = qs.filter(paciente_id=paciente_id)
        if fecha:
            qs = qs.filter(fecha=fecha)
        if estado:
            qs = qs.filter(estado=estado)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidad.objects.all()
        context['medicos'] = Medico.objects.all()
        context['pacientes'] = Paciente.objects.all()
        context['filtros'] = {
            'especialidad': self.request.GET.get('especialidad'),
            'medico': self.request.GET.get('medico'),
            'paciente': self.request.GET.get('paciente'),
            'fecha': self.request.GET.get('fecha'),
            'estado': self.request.GET.get('estado'),
        }
        return context


class TurnoCreateView(LoginRequiredMixin, CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turnos/crear_turno.html'

    def get_success_url(self):
        return redirect('turnos:lista_turnos').url
