from typing import List
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from monitoreo.models import tblsensor
# Create your views here.
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
    