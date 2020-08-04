import django_filters
from .models import QSE,Convenio,Obra


class QSEFilter(django_filters.FilterSet):
    nro = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = QSE
        fields = ['nro','brigada','aprobacion']


class ConvenioFilter(django_filters.FilterSet):
    obra=django_filters.ModelChoiceFilter(queryset=Obra.objects.all())
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Convenio
        fields = ['obra','codigo','descripcion']
