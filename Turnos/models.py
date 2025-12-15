from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100,unique=True,error_messages={'unique': 'Ya existe esta Especialidad.'})

    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        related_name='medicos'
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True,error_messages={'unique': 'Ya existe un paciente con este DNI.'})
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.dni})"


class Turno(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADO', 'Confirmado'),
        ('CANCELADO', 'Cancelado'),
    ]

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='PENDIENTE'
    )

    class Meta:
        unique_together = ('medico', 'fecha', 'hora')

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.medico}"
