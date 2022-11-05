from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from monitoreo.models import tblsensore
from monitoreo.forms import SensoresForm, agregarSensorForm,modificarSensorForm
from monitoreo.filters import sensorFilter
# Create your views here.

def index(request):
    return render(request, 'index.html')

def vista_monitoreo(request):
    #renderiza el template
    vistaMon = tblsensore.objects.all()
    return render(request, 'monitoreo.html',
                    {
                        'vistaMon': vistaMon
                    })
    #para mostrar con una lista 
    #vista_Monitoreo = list(vista_monitoreo.objects.all())
    #return JsonResponse(vista_Monitoreo, safe=False)
    
    #retorna en la vista /monitoreo
    #return HttpResponse("AQUI VA EL MONITOREO")

def vista_monitoreo_edit(request, id):
    sensores = get_object_or_404(tblsensore, id=id)

    data = {
        'form': SensoresForm(instance=sensores)
    }
    if request.method == 'POST':
        formulario = SensoresForm(data=request.POST, instance=sensores, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_sensor")
        data["form"] = formulario



    return render(request, 'sensores/modificar.html', data)

def vista_monitoreo_agregar(request):
    #sensores= tblsensor.objects.get(id=id)
    data = {
        'form': agregarSensorForm()
    }
    if request.method == 'POST':
        formulario = SensoresForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            if formulario.save():
                return redirect(to="listar_sensor")


        data["form"] = formulario


    return render(request, 'sensores/agregar.html', data)

def vista_monitoreo_listar(request):
    sensores = tblsensore.objects.all()
    sensor = sensorFilter(request.GET, queryset=sensores)
    data={
        'filter': sensor,

    }
    return render(request, 'sensores/listar.html', data)

def vista_monitoreo_eliminar(request,id):
    sensores = get_object_or_404(tblsensore, id=id)
    sensores.delete()
    return redirect(to="listar_sensor")

# def is_valid_queryparam(param):
#     return param != '' and param is not None
#
# def filtrar_monitoreo(request):
#     sr = tblsensore.objects.all()
#     codigoSensor_query = request.GET.get('codigoSensor')
#     if is_valid_queryparam(codigoSensor_query):
#         sr = sr.filter(codigoSensor=codigoSensor_query)
#
#
#     return sr

# def vista_monitoreo_filtrar(request):
#     sr = filtrar_monitoreo(request)
#     data = {
#         'sensoress': sr
#     }
#     return render(request, "sensores/listar.html", data)