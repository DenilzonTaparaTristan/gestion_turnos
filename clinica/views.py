from django.shortcuts import render, redirect
from .models import Turno, Paciente, Medico
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required

#PAGINA DE INICIO
@login_required
def index(request):
    return render(request, 'index.html')


#ASIGNAR TURNO
def asignar_turno(request):
    if request.method == "POST":
        paciente_id = request.POST['paciente']
        medico_id = request.POST['medico']
        fecha = request.POST['fecha']
        hora = request.POST['hora']

        paciente = Paciente.objects.get(id=paciente_id)
        medico = Medico.objects.get(id=medico_id)

        # Validar que no haya un turno en la misma fecha y hora
        if Turno.objects.filter(medico=medico, fecha=fecha, hora=hora).exists():
            messages.error(request, "El médico no está disponible en esa fecha y hora.")
        else:
            Turno.objects.create(paciente=paciente, medico=medico, fecha=fecha, hora=hora)
            messages.success(request, "Turno asignado exitosamente.")
            return redirect('index')

    # Asegúrate de enviar pacientes y medicos
    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    return render(request, 'asignar_turno.html', {'pacientes': pacientes, 'medicos': medicos})
#REGISTRAR_PACIENTE
def registrar_paciente(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        dni = request.POST['dni']
        direccion = request.POST['direccion']
        email = request.POST['email']
        telefono = request.POST['telefono']

        # Guardar paciente
        Paciente.objects.create(
            nombre=nombre,
            apellidos=apellidos,
            dni=dni,
            direccion=direccion,
            email=email,
            telefono=telefono
        )
        messages.success(request, "Paciente registrado exitosamente.")
        return redirect('index')

    return render(request, 'registrar_paciente.html')

#LISTAR TURNOS
def listar_turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'listar_turnos.html', {'turnos': turnos})


#REPROGRAMAR TURNO
def reprogramar_turno(request):
    if request.method == "POST":
        turno_id = request.POST['turno_id']
        nueva_fecha = request.POST['fecha']
        nueva_hora = request.POST['hora']
        
        try:
            turno = Turno.objects.get(id=turno_id)
            # Validar disponibilidad
            if Turno.objects.filter(medico=turno.medico, fecha=nueva_fecha, hora=nueva_hora).exists():
                messages.error(request, "El médico no está disponible en esa fecha y hora.")
            else:
                turno.fecha = nueva_fecha
                turno.hora = nueva_hora
                turno.estado = 'confirmado'
                turno.save()
                messages.success(request, "Turno reprogramado exitosamente.")
                return redirect('listar_turnos')
        except Turno.DoesNotExist:
            messages.error(request, "El turno no existe.")
    
    turnos = Turno.objects.all()
    return render(request, 'reprogramar_turno.html', {'turnos': turnos})


#GENERAR REPORTES
def generar_reportes(request):
    reportes = Turno.objects.values('estado').annotate(total=Count('estado'))
    return render(request, 'generar_reportes.html', {'reportes': reportes})


# Elimina esta línea fuera de contexto
# print(f"Notificación enviada: Turno confirmado para {paciente.nombre} el {fecha} a las {hora}.")
