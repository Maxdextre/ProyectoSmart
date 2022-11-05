from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

#AQui se crea las tablas para la Base Datos
# class tblnodo(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     descripcion = models.CharField(max_length=200)
#     sector = models.CharField(max_length=100)
#
#     def __str__(self):
#         return  self.sector

# class tblred(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ip = models.CharField(max_length=15)
#     gateway = models.CharField(max_length=20)
#     mascara = models.CharField(max_length=15)
#     ip_zona = models.CharField(max_length=12)
#     nodo = models.ForeignKey(tblnodo, on_delete=models.CASCADE)

# class tblubicacion(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     latitud = models.CharField(max_length=80)
#     longitud = models.CharField(max_length=80)
#     referencia = models.CharField(max_length=200)
#     def __str__(self):
#         return self.latitud + ' | '+ self.longitud

# class tbltipo_sensor(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     detalle = models.CharField(max_length=200)
#     def __str__(self):
#         return self.nombre
# class tblbateria(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nivel = models.IntegerField()
#     estado = models.BooleanField(default=True)

class tblsensore(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo= models.CharField(max_length=6)
    descripcion= models.CharField(max_length=200)
    #red = models.ForeignKey(tblred,on_delete=models.CASCADE)
    #tip_sensor = models.ForeignKey(tbltipo_sensor, on_delete=models.CASCADE)
    #ubicaciones = models.ForeignKey(tblubicacion, on_delete=models.CASCADE)
    nivel_bateria = models.IntegerField()
    estado_bateria = models.BooleanField(default=True)
    tipo_sensor = models.CharField(max_length=100)
    detalle_sensor = models.CharField(max_length=200)
    latitud_ubicacion = models.CharField(max_length=80)
    longitud_ubicacion = models.CharField(max_length=80)
    referencia_ubicacion = models.CharField(max_length=200)

    ip_red = models.CharField(max_length=15)
    gateway_red = models.CharField(max_length=20)
    mascara_red = models.CharField(max_length=15)
    ip_zona_red = models.CharField(max_length=12)
    descripcion_nodo = models.CharField(max_length=200)
    sector_nodo = models.CharField(max_length=100)


    def __str__(self):
        return self.id
