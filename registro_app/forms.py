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