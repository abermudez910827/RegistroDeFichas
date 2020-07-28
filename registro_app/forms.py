from django.forms import ModelForm
from .models import Persona,Convenio,Especialidad,Brigada,QSE,Actividad,Zona,Objeto,Obra,MesEnCurso

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre']

class EspecialidadForm(ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']

class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['codigo','descripcion']

class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre','descripcion']

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre','descripcion']

class BrigadaForm(ModelForm):
    class Meta:
        model = Brigada
        fields = ['nombre','jefe','integrantes']

class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields = ['nombre','objetos']

class ObjetoForm(ModelForm):
    class Meta:
        model = Objeto
        fields = ['nombre']

class QSEForm(ModelForm):
    class Meta:
        model = QSE
        fields = ['nro',
        'especialidad',
        'convenio',
        'actividad',
        'brigada',
        'zona',
        'objeto',
        'clasificacion',
        'mes_en_curso',
        'fecha',
        'aprobacion',
        'observaciones']     