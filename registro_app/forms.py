from django.forms import ModelForm, TextInput, Textarea, DateInput, CheckboxInput, Select, SelectMultiple, CheckboxSelectMultiple
from .models import Persona, Convenio, Especialidad, Brigada, QSE, Actividad, Zona, Objeto, Obra, MesEnCurso


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre']
        labels = {
            'name': ('Nombre'),
        }
        help_texts = {
            'name': ('Nombre de la persona.'),
        }
        error_messages = {
            'name': {
                'max_length': ("El nombre es muy largo."),
            },
        }
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
        }


class EspecialidadForm(ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
        }


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['codigo', 'descripcion']
        labels = {
            'codigo': ('Código'),
            'descripcion': ('Descripción'),
        }
        widgets = {
            'codigo': TextInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'class': 'form-control'})

        }


class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': ('Nombre'),
            'descripcion': ('Descripción'),
        }
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'class': 'form-control'})
        }


class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': ('Nombre'),
            'descripcion': ('Descripción'),
        }
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'class': 'form-control'})
        }


class BrigadaForm(ModelForm):
    class Meta:
        model = Brigada
        fields = ['nombre', 'jefe', 'integrantes']
        labels = {
            'nombre': ('Nombre'),
            'jefe': ('Jefe'),
            'integrantes': ('Integrantes'),
        }
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'jefe': Select(attrs={'class': 'form-control'}),
            'integrantes': SelectMultiple(attrs={'class': 'form-control'})
        }


class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields = ['nombre', 'objetos']
        labels = {
            'nombre': ('Nombre'),
            'objetos': ('Objetos'),
        }
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'objetos': SelectMultiple(attrs={'class': 'form-control'})
        }


class ObjetoForm(ModelForm):
    class Meta:
        model = Objeto
        fields = ['nombre']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'})
        }


class MesEnCursoForm(ModelForm):
    class Meta:
        model = MesEnCurso
        fields = ['mes', 'anno', 'obra']
        widgets = {
            'mes': Select(attrs={'class': 'form-control'}),
            'anno': TextInput(attrs={'class': 'form-control'}),
            'objetos': Select(attrs={'class': 'form-control'})
        }


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

        labels = {
            'aprobacion': ('Aprobación'),
        }
        widgets = {
            'nro': TextInput(attrs={'class': 'form-control'}),
            'especialidad': Select(attrs={'class': 'form-control'}),
            'convenio': Select(attrs={'class': 'form-control'}),
            'actividad': Select(attrs={'class': 'form-control'}),
            'brigada': Select(attrs={'class': 'form-control'}),
            'zona': Select(attrs={'class': 'form-control'}),
            'objeto': Select(attrs={'class': 'form-control'}),
            'clasificacion': TextInput(attrs={'class': 'form-control'}),
            'mes_en_curso': Select(attrs={'class': 'form-control'}),
            'fecha': DateInput(attrs={'class': 'form-control'}),
            'aprobacion': CheckboxInput(attrs={'class': 'form-control '}),
            'observaciones': Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['objeto'].queryset = Objeto.objects.none()

        if 'zona' in self.data:
            try:
                zona_id = int(self.data.get('zona'))
                self.fields['objeto'].queryset = Objeto.objects.filter(
                    zona=zona_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty objeto queryset
        elif self.instance.pk:
            self.fields['objeto'].queryset = Objeto.objects.filter(
                zona=self.instance.zona.pk).order_by('nombre')
            # self.instance.zona.objeto_set.order_by('nombre')
