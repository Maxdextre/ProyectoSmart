from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    #path('monitoreo/', views.vista_monitoreo, name="monitoreo"),
    path('edit-sensor/<id>/', views.vista_monitoreo_edit, name="editar_sensor"),
    path('agregar-sensor/', views.vista_monitoreo_agregar, name="agregar_sensor"),
    path('listar-sensor/', views.vista_monitoreo_listar, name="listar_sensor"),
    path('eliminar-sensor/<id>', views.vista_monitoreo_eliminar, name="eliminar_sensor"),
]