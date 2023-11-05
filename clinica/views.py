from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Paciente, Medico, Mensaje, Cita
import datetime, locale
from random import choice

# Create your views here.

def inicio(request):
    return render(request, "home.html")

#Views del personal administrativo
def staffmenu(request):
    return render(request,"staffmenu.html")

def pacientes(request):

    lista_pacientes=Paciente.objects.all()
    return render(request, "pacientes.html",{'lista_pacientes':lista_pacientes})

def pacientesguardar(request):
    nombre= request.POST["nombre"]
    dpi=request.POST["dpi"]
    telefono=request.POST["telefono"]
    nacimiento=request.POST["nacimiento"]
    direccion=request.POST["direccion"]
    fecha_cita=request.POST["fecha_cita"]
    razon_cita=request.POST["razon_cita"]
    receta=request.POST["receta"]
    diagnostico = request.POST["diagnostico"]

    lista_pacientes=Paciente.objects.all()  
    if any(int(dpi) == int(objeto.dpi) for objeto in lista_pacientes):
        messages.success(request, 'El registro ya existe')
    else:
        p = Paciente(nombre=nombre, dpi=dpi, telefono=telefono, nacimiento=nacimiento, direccion=direccion, fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, diagnostico=diagnostico)
        p.save()
        messages.success(request, 'El paciente ha sido agregado')
    return redirect('pacientes')

def pacienteseliminar(request, id):

    paciente = Paciente.objects.filter(pk=id)
    paciente.delete()
    messages.success(request, 'El paciente ha sido eliminado')

    return redirect('pacientes')

def pacientesmostrar(request, id):
    paciente = Paciente.objects.get(pk=id)
    return render(request, "pacienteseditar.html", {'paciente':paciente})

def pacientesmodificar(request):

    nombre= request.POST["nombre"]
    dpi=request.POST["dpi"]
    telefono=request.POST["telefono"]
    nacimiento=request.POST["nacimiento"]
    direccion=request.POST["direccion"]
    fecha_cita=request.POST["fecha_cita"]
    razon_cita=request.POST["razon_cita"]
    receta=request.POST["receta"]
    diagnostico = request.POST["diagnostico"]
    id = request.POST["id"]

    Paciente.objects.filter(pk=id).update(id=id,nombre=nombre, dpi=dpi, telefono=telefono, nacimiento=nacimiento, direccion=direccion, fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, diagnostico=diagnostico)
    messages.success(request, 'El paciente ha sido modificado')
    if fecha_cita and razon_cita:
            lista_doctores = []
            for medico in Medico.objects.all():
                lista_doctores.append(medico.nombre)
            doctor=choice(lista_doctores)
            c = Cita(nombre=nombre, dpi=dpi, fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, diagnostico=diagnostico, doctor=doctor)
            c.save()
            messages.success(request, 'Cita agregada')
    return redirect('pacientes')

def medicos(request):
    lista_medicos=Medico.objects.all()
    return render(request, "medicos.html",{'lista_medicos':lista_medicos} )

def medicosguardar(request):
    nombre= request.POST["nombre"]
    colegiado=request.POST["colegiado"]
    especialidad=request.POST["especialidad"]

    p = Medico(nombre=nombre, colegiado=colegiado, especialidad=especialidad)
    p.save()
    messages.success(request, 'El Medico ha sido agregado')

    return redirect('medicos')

def medicoseliminar(request, id):

    medico = Medico.objects.filter(pk=id)
    medico.delete()
    messages.success(request, 'El medico ha sido eliminado')

    return redirect('medicos')

def medicosmostrar(request, id):

    medico = Medico.objects.get(pk=id)
    return render(request, "medicoseditar.html", {'medico':medico})

def medicosmodificar(request):
    nombre= request.POST["nombre"]
    colegiado=request.POST["colegiado"]
    especialidad=request.POST["especialidad"]

    id = request.POST["id"]

    Medico.objects.filter(pk=id).update(id=id,nombre=nombre, colegiado=colegiado, especialidad=especialidad)
    messages.success(request, 'El medico ha sido modificado')
    return redirect('medicos')

#Views del usuario

def usuariomenu(request):
    return render(request, "usuariomenu.html")

def usuarioregistro(request):
    return render(request, "usuarioregistro.html")

def usuarioregistrar(request):

    nombre= request.POST["nombre"]
    dpi=request.POST["dpi"]
    telefono=request.POST["telefono"]
    nacimiento=request.POST["nacimiento"]
    direccion=request.POST["direccion"]
    fecha_cita=request.POST["fecha_cita"]
    razon_cita=request.POST["razon_cita"]
    receta=""
    diagnostico =""

    lista_pacientes = Paciente.objects.all()
    if any(int(dpi) == int(objeto.dpi) for objeto in lista_pacientes):
        messages.success(request, 'El registro ya existe')
        return redirect('usuarioregistro')
    else:
        p = Paciente(nombre=nombre, dpi=dpi, nacimiento=nacimiento, direccion=direccion, fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, telefono=telefono, diagnostico=diagnostico)
        p.save()
        messages.success(request, 'Te has registrado como paciente')
        if fecha_cita and razon_cita:
            lista_doctores = []
            for medico in Medico.objects.all():
                lista_doctores.append(medico.nombre)
            doctor=choice(lista_doctores)
            c = Cita(nombre=nombre, dpi=dpi, fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, diagnostico=diagnostico, doctor=doctor)
            c.save()
            messages.success(request, 'Cita agregada')
        return redirect('usuariomenu')

def usuariomensaje(request):
    return render(request,"usuariomensaje.html")

def usuarioenviarmensaje(request):
    nombre = request.POST["nombre"]
    telefono=request.POST["telefono"]
    asunto = request.POST["asunto"]
    contenido = request.POST["contenido"]
    
    locale.setlocale(locale.LC_TIME, 'es_LA.UTF-8')
    fecha_actual = datetime.datetime.now()
    fecha = fecha_actual.strftime("%d de %B de %Y")

    m = Mensaje(nombre=nombre, telefono=telefono, fecha=fecha, asunto=asunto, contenido=contenido)
    m.save()
    messages.success(request, 'El mensaje ha sido enviado')
    return redirect('usuariomensaje')

#Views del staff que deberian de estar arriba pero me da weba cambiarles el nombre como a 1 millon de metodos
def staffbuzon(request):
    mensajes = Mensaje.objects.all()
    return render(request, "staffbuzon.html", {'mensajes':mensajes})

def staffcitas(request):
    citas = Cita.objects.all()
    return render(request, "staffcitas.html",{'citas':citas})

def staffcitasguardar(request):
    nombre= request.POST["nombre"]
    dpi=request.POST["dpi"]
    fecha_cita=request.POST["fecha_cita"]
    razon_cita=request.POST["razon_cita"]
    receta=request.POST["receta"]
    diagnostico = request.POST["diagnostico"]
    doctor= request.POST["doctor"]

    lista_pacientes=Paciente.objects.all()
    if any(int(dpi) == int(objeto.dpi) for objeto in lista_pacientes):
        c = Cita(nombre=nombre, dpi=dpi, fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, diagnostico=diagnostico, doctor=doctor)
        c.save()
        messages.success(request, 'Cita agregada')
    else:
        messages.success(request, 'Registre el paciente antes de agendar una cita')
    return redirect('staffcitas')

def staffcitaseliminar(request, id):
    c = Cita.objects.filter(pk=id)
    c.delete()
    messages.success(request, 'Registro eliminado')

    return redirect('staffcitas')

def staffcitasmostrar(request, id):
    citas = Cita.objects.get(pk=id)
    return render(request, "staffcitaseditar.html", {'citas':citas})

def staffcitasmodificar(request):
    
    nombre= request.POST["nombre"]
    dpi=request.POST["dpi"]
    fecha_cita=request.POST["fecha_cita"]
    razon_cita=request.POST["razon_cita"]
    receta=request.POST["receta"]
    diagnostico = request.POST["diagnostico"]
    doctor= request.POST["doctor"]
    id = request.POST["id"] 

    Cita.objects.filter(pk=id).update(id=id,nombre=nombre, dpi=dpi,fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, diagnostico=diagnostico, doctor=doctor)
    messages.success(request, 'Cita modificada con exito')
    return redirect('staffcitas')

def usuariocita(request):
    return render(request, "usuariocita.html")  

def usuariocitaguardar(request):
    nombre= request.POST["nombre"]
    dpi=request.POST["dpi"]
    fecha_cita=request.POST["fecha_cita"]
    razon_cita=request.POST["razon_cita"]
    receta=""
    diagnostico = ""
    doctor= ""

    lista_doctores = []
    for medico in Medico.objects.all():
        lista_doctores.append(medico.nombre)
    doctor=choice(lista_doctores)

    lista_pacientes=Paciente.objects.all()
    if any(str(nombre)==str(objeto.nombre) and int(dpi) == int(objeto.dpi) for objeto in lista_pacientes):

        c = Cita(nombre=nombre, dpi=dpi, fecha_cita=fecha_cita, razon_cita=razon_cita, receta=receta, diagnostico=diagnostico, doctor=doctor)
        c.save()
        messages.success(request, 'Cita agregada')
        
    else:
        messages.success(request, 'Paciente no registrado o nombre no coincide')
    return redirect('usuariocita')

def ingresar(request):
    return render(request, "staffcontraseña.html")

def verificar(request):
    contra = request.POST['contra']
    if str(contra)=="contra123":
        return redirect('staffmenu')
    else:
        messages.success(request, 'Contraseña incorrecta')
        return render(request, "staffcontraseña.html")