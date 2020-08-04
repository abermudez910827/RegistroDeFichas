import django_filters
from .models import QSE,Convenio


class QSEFilter(django_filters.FilterSet):
    nro = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = QSE
        fields = ['nro','brigada','aprobacion']


class ConvenioFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Convenio
        fields = ['codigo','descripcion']
