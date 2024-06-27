from django.db import models
import datetime

def mayor18(value):
    pass
# Create your models here.
class Conductor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField(validators=[mayor18])
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Direccion(models.Model):
    regiones = (("iii","Atacama"),("v","Valparaiso"),("vi","O'Higgins"),("ix","Araucanía"))
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=regiones)
    conductor = models.OneToOneField(Conductor, related_name='direccion', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.calle} {self.numero}, {self.comuna}, {self.region}'

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    agno = models.DateField(default=datetime.date.today)
    conductor = models.ForeignKey(Conductor, related_name='vehiculos', on_delete=models.CASCADE)