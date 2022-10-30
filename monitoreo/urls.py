from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('monitoreo/', views.vista_monitoreo),
]