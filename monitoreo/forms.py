from django import forms
from .models import tblsensor, tblred,tblnodo,tblbateria,tblubicacion,tbltipo_sensor

class SensoresForm(forms.ModelForm):


    class Meta:
        model = tblsensor
        # fields = ["codigo", "descripcion"]
        # model2 = tblsensor.red
        # fields2 = ["ip"]
        # model4 = tblsensor.ubicaciones
        # fields5 = ["latitud"]
        # model6 = tblsensor.red.nodo
        # fields3 = ["sector"]
        # model3 = tblsensor.bateria
        # fields4 = ["nivel"]
        # model5 = tblsensor.tip_sensor
        # fields6 = ["nombre"]

        fields = ["codigo", "descripcion"]


        #fields = ["codigo", "nombre", "latitud", "longitud", "sector", "descripcion", "nivel", "ip"]
        #fields = '__all__'