from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True, null=True, blank=True)  # Campo para DNI
    direccion = models.CharField(max_length=255, default="Sin dirección")     # Campo para Dirección
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    historial_citas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - DNI: {self.dni}"


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)
    horario_disponible = models.TextField()

    def __str__(self):
        return f"Dr. {self.nombre} - {self.especialidad}"

class Turno(models.Model):
    ESTADOS = [('pendiente', 'Pendiente'), ('confirmado', 'Confirmado'), ('cancelado', 'Cancelado')]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.estado}"

class Notificacion(models.Model):
    TURNO_TIPO = [('SMS', 'SMS'), ('EMAIL', 'Correo Electrónico')]
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TURNO_TIPO)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.turno} - {self.tipo}"
