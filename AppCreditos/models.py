from django.db import models

# Create your models here.

class Creditos(models.Model):
    nro_cred = models.IntegerField()
    fecha = models.DateField()
    importe = models.FloatField()
    cuotas = models.IntegerField()
        
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha_nac = models.DateField()
    
class Comercio(models.Model):
    nombre_com = models.CharField(max_length=40)
    rubro = models.CharField(max_length=40)