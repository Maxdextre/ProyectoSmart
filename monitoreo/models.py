from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
#AQui se crea las tablas para la Base Datos
class tblnodo(models.Model):
    descripcion = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
class tblred(models.Model):
    ip = models.CharField(max_length=15)
    gateway = models.CharField(max_length=20)
    mascara = models.CharField(max_length=15)
    ip_zona = models.CharField(max_length=12)
    nodo = models.ForeignKey(tblnodo, on_delete=models.CASCADE)

class tblubicacion(models.Model):
    latitud = models.CharField(max_length=80)
    longitud = models.CharField(max_length=80)
    referencia = models.CharField(max_length=200)

class tbltipo_sensor(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=200)

class tblbateria(models.Model):
    nivel = models.IntegerField()
    estado = models.BooleanField(default=True)

class tblsensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo= models.CharField(max_length=6)
    descripcion= models.CharField(max_length=200)
    #tipo= models.CharField(max_length=200) #tipo 2
    #ubicacion= models.CharField(max_length=200)
    #nodo= models.CharField(max_length=200) #ubicacion calle san luis
    #descripcion= models.CharField(max_length=200)
    #estado = models.BooleanField(default=True)
    red = models.ForeignKey(tblred,on_delete=models.CASCADE)
    bateria = models.ForeignKey(tblbateria, on_delete=models.CASCADE)
    tip_sensor = models.ForeignKey(tbltipo_sensor, on_delete=models.CASCADE)
    ubicaciones = models.ForeignKey(tblubicacion, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codigo + ' - '+ self.tip_sensor.nombre + ' - ' + self.red.nodo.sector
    



