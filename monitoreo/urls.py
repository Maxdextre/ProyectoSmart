from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('monitoreo/', views.vista_monitoreo),
    path('edit-sensor/<id>/', views.vista_monitoreo_edit, name="editar_sensor"),
]