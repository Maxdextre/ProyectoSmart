from django import forms
from .models import tblsensore

class SensoresForm(forms.ModelForm):

    #P     nombres = forms.ModelChoiceField(queryset=tbltipo_sensor.objects.values('nombre'), initial=0, to_field_name="nombre")
    class Meta:
        model = tblsensore

        fields = '__all__'


        #fields = ["codigo", "nombre", "latitud", "longitud", "sector", "descripcion", "nivel", "ip"]
        #fields = '__all__'

class agregarSensorForm(forms.ModelForm):

    #name_nodo = forms.CharField(tblnodo)
    class Meta:
        model = tblsensore
        fields = ["codigo", "tipo_sensor", "latitud_ubicacion", "longitud_ubicacion", "descripcion_nodo", "descripcion", "nivel_bateria", "ip_red"]

class modificarSensorForm(forms.ModelForm):
    #name_nodo = forms.CharField(tblnodo)
    class Meta:
        model = tblsensore
        fields = ["codigo", "tipo_sensor", "longitud_ubicacion", "longitud_ubicacion", "descripcion_nodo", "descripcion", "nivel_bateria", "ip_red"]

