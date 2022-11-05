import django_filters
from monitoreo.models import tblsensore

class sensorFilter(django_filters.FilterSet):

    class Meta:
        model = tblsensore
        fields = ['codigo']
