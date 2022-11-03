from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from monitoreo.models import tblsensor
from .forms import SensoresForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def vista_monitoreo(request):
    #renderiza el template
    vistaMon = tblsensor.objects.all()
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
    sensores = get_object_or_404(tblsensor, id=id)

    data = {
        'form': SensoresForm(instance=sensores)
    }
    if request.method == 'POST':
        formulario = SensoresForm(data=request.POST, instance=sensores, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return  redirect(to="monitoreo")
        data["form"] = formulario
    return render(request, 'sensores/modificar.html', data)