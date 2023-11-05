from django.db import models
# Create your models here.

class Paciente(models.Model):
    
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()
    dpi=models.IntegerField()
    nacimiento=models.CharField(max_length=10)
    direccion=models.CharField(max_length=30)
    fecha_cita=models.CharField(max_length=10,null=True, blank=True)
    razon_cita=models.TextField(max_length=100, null=True, blank=True)
    receta=models.TextField(max_length=100, null=True, blank=True)
    diagnostico=models.TextField(max_length=100, null=True, blank=True)

class Medico(models.Model):

    nombre=models.CharField(max_length=30)
    colegiado=models.IntegerField()
    especialidad=models.CharField(max_length=30)


class Mensaje(models.Model):
    
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    fecha = models.CharField(max_length=10)
    asunto = models.CharField(max_length=30)
    contenido = models.TextField(max_length=300)

class Cita(models.Model):

    nombre=models.CharField(max_length=30)
    dpi=models.IntegerField()
    fecha_cita=models.CharField(max_length=10)
    razon_cita=models.TextField(max_length=100)
    receta=models.TextField(max_length=100, null=True, blank=True)
    diagnostico=models.TextField(max_length=100, null=True, blank=True)
    doctor=models.CharField(max_length=30, null=True, blank=True)

