from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as v_login, logout as v_logout
from .forms import UploadExcelForm, PersonaForm, EspecialidadForm, ActividadForm, ObraForm, BrigadaForm, ObjetoForm, ZonaForm, ConvenioForm, MesEnCursoForm, QSEForm
from .models import Persona, Convenio, Especialidad, Brigada, QSE, Actividad, Zona, Objeto, Obra, MesEnCurso
from openpyxl import load_workbook
from .filters import QSEFilter, ConvenioFilter


def index(request):
    return render(request, 'registro_app/index.html', {'active_index': True})


def signupuser(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm, 'active_signup': True})
    else:
        # Creacion de usuario
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                v_login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm, 'error': 'El usuario ya existe', 'active_signup': True})

        else:
            # Contrasena no coincide
            return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden', 'active_signup': True})


def denegado(request):
    return render(request, 'registro_app/errors/505.html')


def logout(request):
    if request.method == 'POST':
        v_logout(request)
        return redirect('index')


def login(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/index.html', {'form': AuthenticationForm(), 'active_index': True})
    else:
        # Login de usuario
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'registro_app/index.html', {'form': AuthenticationForm(), 'error': 'Usuario o contraseña incorrecta', 'active_index': True})
        else:
            v_login(request, user)
            return redirect('index')

# Personas


def persona_index(request):
    personas = Persona.objects.all()
    return render(request, 'registro_app/persona/index.html', {'personas': personas, 'active_personas': True, 'active_datos': True})


@login_required(login_url='/')
def persona_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/persona/create.html', {'form': PersonaForm(), 'active_personas': True, 'active_datos': True})
    else:
        persona = PersonaForm(request.POST)
        if persona.is_valid():
            persona.save()
            return redirect('personas')
        return render(request, 'registro_app/persona/create.html', {'form': persona, 'active_personas': True, 'active_datos': True})


@login_required(login_url='/')
def persona_edit(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)

    if(request.method == 'GET'):
        form = PersonaForm(instance=persona)
        return render(request, 'registro_app/persona/edit.html', {'form': form, 'active_personas': True, 'active_datos': True})
    else:
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona_view', persona.id)
        return render(request, 'registro_app/persona/edit.html', {'form': form, 'active_personas': True, 'active_datos': True})


def persona_view(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    return render(request, 'registro_app/persona/view.html', {'persona': persona, 'active_personas': True, 'active_datos': True})


@login_required(login_url='/')
def persona_delete(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    if (request.method == 'POST'):
        persona.delete()
    return redirect('personas')

 # Especialidades


def especialidad_index(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'registro_app/especialidad/index.html', {'especialidades': especialidades, 'active_especialidades': True, 'active_datos': True})


@login_required(login_url='/')
def especialidad_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/especialidad/create.html', {'form': EspecialidadForm(), 'active_especialidades': True, 'active_datos': True})
    else:
        especialidad = EspecialidadForm(request.POST)
        if especialidad.is_valid():
            especialidad.save()
            return redirect('especialidades')
        return render(request, 'registro_app/especialidad/create.html', {'form': especialidad, 'active_especialidades': True, 'active_datos': True})


@login_required(login_url='/')
def especialidad_edit(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, pk=especialidad_id)

    if(request.method == 'GET'):
        form = EspecialidadForm(instance=especialidad)
        return render(request, 'registro_app/especialidad/edit.html', {'form': form, 'active_especialidades': True, 'active_datos': True})
    else:
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('especialidad_view', especialidad.id)
        return render(request, 'registro_app/especialidad/edit.html', {'form': form, 'active_especialidades': True, 'active_datos': True})


def especialidad_view(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, pk=especialidad_id)
    return render(request, 'registro_app/especialidad/view.html', {'especialidad': especialidad, 'active_especialidades': True, 'active_datos': True})


@login_required(login_url='/')
def especialidad_delete(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, pk=especialidad_id)
    if (request.method == 'POST'):
        especialidad.delete()
    return redirect('especialidades')

# actividades


def actividad_index(request):
    actividades = Actividad.objects.all()
    return render(request, 'registro_app/actividad/index.html', {'actividades': actividades, 'active_actividades': True, 'active_datos': True})


@login_required(login_url='/')
def actividad_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/actividad/create.html', {'form': ActividadForm(), 'active_actividades': True, 'active_datos': True})
    else:
        actividad = ActividadForm(request.POST)
        if actividad.is_valid():
            actividad.save()
            return redirect('actividades')
        return render(request, 'registro_app/actividad/create.html', {'form': actividad, 'active_actividades': True, 'active_datos': True})


@login_required(login_url='/')
def actividad_edit(request, actividad_id):
    actividad = get_object_or_404(Actividad, pk=actividad_id)

    if(request.method == 'GET'):
        form = ActividadForm(instance=actividad)
        return render(request, 'registro_app/actividad/edit.html', {'form': form, 'active_actividades': True, 'active_datos': True})
    else:
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividad_view', actividad.id)
        return render(request, 'registro_app/actividad/edit.html', {'form': form, 'active_actividades': True, 'active_datos': True})


def actividad_view(request, actividad_id):
    actividad = get_object_or_404(Actividad, pk=actividad_id)
    return render(request, 'registro_app/actividad/view.html', {'actividad': actividad, 'active_actividades': True, 'active_datos': True})


@login_required(login_url='/')
def actividad_delete(request, actividad_id):
    actividad = get_object_or_404(Actividad, pk=actividad_id)
    if (request.method == 'POST'):
        actividad.delete()
    return redirect('actividades')

# Obras


def obra_index(request):
    obras = Obra.objects.all()
    return render(request, 'registro_app/obra/index.html', {'obras': obras, 'active_obras': True})


@login_required(login_url='/')
def obra_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/obra/create.html', {'form': ObraForm(), 'active_obras': True})
    else:
        obra = ObraForm(request.POST)
        if obra.is_valid():
            obra.save()
            return redirect('obras')
        return render(request, 'registro_app/obra/create.html', {'form': obra, 'active_obras': True})


@login_required(login_url='/')
def obra_edit(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)

    if(request.method == 'GET'):
        form = ObraForm(instance=obra)
        return render(request, 'registro_app/obra/edit.html', {'form': form, 'active_obras': True})
    else:
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('obra_view', obra.id)
        return render(request, 'registro_app/obra/edit.html', {'form': form, 'active_obras': True})


def obra_view(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    return render(request, 'registro_app/obra/view.html', {'obra': obra, 'active_obras': True})


@login_required(login_url='/')
def obra_delete(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    if (request.method == 'POST'):
        obra.delete()
    return redirect('obras')

# Objetos


def objeto_index(request):
    objetos = Objeto.objects.all()
    return render(request, 'registro_app/objeto/index.html', {'objetos': objetos, 'active_objetos': True, 'active_datos': True})


def load_objetos(request):
    zona_id = request.GET.get('zona')
    objetos = Objeto.objects.filter(zona=zona_id).order_by('nombre')
    print(objetos)
    return render(request, 'registro_app/components/objeto_dropdown_list_options.html', {'objetos': objetos})


@login_required(login_url='/')
def objeto_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/objeto/create.html', {'form': ObjetoForm(), 'active_objetos': True, 'active_datos': True})
    else:
        objeto = ObjetoForm(request.POST)
        if objeto.is_valid():
            objeto.save()
            return redirect('objetos')
        return render(request, 'registro_app/objeto/create.html', {'form': objeto, 'active_objetos': True, 'active_datos': True})


@login_required(login_url='/')
def objeto_edit(request, objeto_id):
    objeto = get_object_or_404(Objeto, pk=objeto_id)

    if(request.method == 'GET'):
        form = ObjetoForm(instance=objeto)
        return render(request, 'registro_app/objeto/edit.html', {'form': form, 'active_objetos': True, 'active_datos': True})
    else:
        form = ObjetoForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect('objeto_view', objeto.id)
        return render(request, 'registro_app/objeto/edit.html', {'form': form, 'active_objetos': True, 'active_datos': True})


def objeto_view(request, objeto_id):
    objeto = get_object_or_404(Objeto, pk=objeto_id)
    return render(request, 'registro_app/objeto/view.html', {'objeto': objeto, 'active_objetos': True, 'active_datos': True})


@login_required(login_url='/')
def objeto_delete(request, objeto_id):
    objeto = get_object_or_404(Objeto, pk=objeto_id)
    if (request.method == 'POST'):
        objeto.delete()
    return redirect('objetos')

# Zonas


def zona_index(request):
    zonas = Zona.objects.all()
    return render(request, 'registro_app/zona/index.html', {'zonas': zonas, 'active_zonas': True, 'active_datos': True})


@login_required(login_url='/')
def zona_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/zona/create.html', {'form': ZonaForm(), 'active_zonas': True, 'active_datos': True})
    else:
        zona = ZonaForm(request.POST)
        if zona.is_valid():
            zona.save()
            return redirect('zonas')
        return render(request, 'registro_app/zona/create.html', {'form': zona, 'active_zonas': True, 'active_datos': True})


@login_required(login_url='/')
def zona_edit(request, zona_id):
    zona = get_object_or_404(Zona, pk=zona_id)

    if(request.method == 'GET'):
        form = ZonaForm(instance=zona)
        return render(request, 'registro_app/zona/edit.html', {'form': form, 'active_zonas': True, 'active_datos': True})
    else:
        form = ZonaForm(request.POST, instance=zona)
        if form.is_valid():
            form.save()
            return redirect('zona_view', zona.id)
        return render(request, 'registro_app/zona/edit.html', {'form': form, 'active_zonas': True, 'active_datos': True})


def zona_view(request, zona_id):
    zona = get_object_or_404(Zona, pk=zona_id)
    return render(request, 'registro_app/zona/view.html', {'zona': zona, 'active_zonas': True, 'active_datos': True})


@login_required(login_url='/')
def zona_delete(request, zona_id):
    zona = get_object_or_404(Zona, pk=zona_id)
    if (request.method == 'POST'):
        zona.delete()
    return redirect('zonas')

# Brigadas


def brigada_index(request):
    brigadas = Brigada.objects.all()
    return render(request, 'registro_app/brigada/index.html', {'brigadas': brigadas, 'active_brigadas': True, 'active_datos': True})


@login_required(login_url='/')
def brigada_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/brigada/create.html', {'form': BrigadaForm(), 'active_brigadas': True, 'active_datos': True, 'active_datos': True})
    else:
        brigada = BrigadaForm(request.POST)
        if brigada.is_valid():
            brigada.save()
            return redirect('brigadas')
        return render(request, 'registro_app/brigada/create.html', {'form': brigada, 'active_brigadas': True, 'active_datos': True})


@login_required(login_url='/')
def brigada_edit(request, brigada_id):
    brigada = get_object_or_404(Brigada, pk=brigada_id)

    if(request.method == 'GET'):
        form = BrigadaForm(instance=brigada)
        return render(request, 'registro_app/brigada/edit.html', {'form': form, 'active_brigadas': True, 'active_datos': True, 'active_datos': True})
    else:
        form = BrigadaForm(request.POST, instance=brigada)
        if form.is_valid():
            form.save()
            return redirect('brigada_view', brigada.id)
        return render(request, 'registro_app/brigada/edit.html', {'form': form, 'active_brigadas': True, 'active_datos': True, 'active_datos': True})


def brigada_view(request, brigada_id):
    brigada = get_object_or_404(Brigada, pk=brigada_id)
    return render(request, 'registro_app/brigada/view.html', {'brigada': brigada, 'active_brigadas': True, 'active_datos': True})


@login_required(login_url='/')
def brigada_delete(request, brigada_id):
    brigada = get_object_or_404(Brigada, pk=brigada_id)
    if (request.method == 'POST'):
        brigada.delete()
    return redirect('brigadas')

# Convenios


def convenio_index(request):

    # convenios = Convenio.objects.all().order_by('codigo')
    convenios_filter = ConvenioFilter(
        request.GET, queryset=Convenio.objects.all().order_by('codigo'))
    paginator = Paginator(convenios_filter.qs, 50)  # Show 50 per page.
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'registro_app/convenio/index.html', {'convenios': page_obj, 'convenios_filter': convenios_filter, 'active_convenios': True, 'active_datos': True})


@login_required(login_url='/')
def convenio_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/convenio/create.html', {'form': ConvenioForm(), 'active_convenios': True, 'active_datos': True})
    else:
        convenio = ConvenioForm(request.POST)
        if convenio.is_valid():
            convenio.save()
            return redirect('convenios')
        return render(request, 'registro_app/convenio/create.html', {'form': convenio, 'active_convenios': True, 'active_datos': True})


@login_required(login_url='/')
def convenio_edit(request, convenio_id):
    convenio = get_object_or_404(Convenio, pk=convenio_id)

    if(request.method == 'GET'):
        form = ConvenioForm(instance=convenio)
        return render(request, 'registro_app/convenio/edit.html', {'form': form, 'active_convenios': True, 'active_datos': True})
    else:
        form = ConvenioForm(request.POST, instance=convenio)
        if form.is_valid():
            form.save()
            return redirect('convenio_view', convenio.id)
        return render(request, 'registro_app/convenio/edit.html', {'form': form, 'active_convenios': True, 'active_datos': True})


def convenio_view(request, convenio_id):
    convenio = get_object_or_404(Convenio, pk=convenio_id)
    return render(request, 'registro_app/convenio/view.html', {'convenio': convenio, 'active_convenios': True, 'active_datos': True})


@login_required(login_url='/')
def convenio_delete(request, convenio_id):
    convenio = get_object_or_404(Convenio, pk=convenio_id)
    if (request.method == 'POST'):
        convenio.delete()
    return redirect('convenios')

# Mes en Curso


def mes_en_curso_index(request):
    mes_en_cursos = MesEnCurso.objects.all()
    return render(request, 'registro_app/mes_en_curso/index.html', {'mes_en_cursos': mes_en_cursos, 'active_mes_en_cursos': True})


@login_required(login_url='/')
def mes_en_curso_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/mes_en_curso/create.html', {'form': MesEnCursoForm(), 'active_mes_en_cursos': True})
    else:
        mes_en_curso = MesEnCursoForm(request.POST)
        if mes_en_curso.is_valid():
            mes_en_curso.save()
            return redirect('mes_en_cursos')
        return render(request, 'registro_app/mes_en_curso/create.html', {'form': mes_en_curso, 'active_mes_en_cursos': True})


@login_required(login_url='/')
def mes_en_curso_edit(request, mes_en_curso_id):
    mes_en_curso = get_object_or_404(MesEnCurso, pk=mes_en_curso_id)

    if(request.method == 'GET'):
        form = MesEnCursoForm(instance=mes_en_curso)
        return render(request, 'registro_app/mes_en_curso/edit.html', {'form': form, 'active_mes_en_cursos': True})
    else:
        form = MesEnCursoForm(request.POST, instance=mes_en_curso)
        if form.is_valid():
            form.save()
            return redirect('mes_en_curso_view', mes_en_curso.id)
        return render(request, 'registro_app/mes_en_curso/edit.html', {'form': form, 'active_mes_en_cursos': True})


def mes_en_curso_view(request, mes_en_curso_id):
    mes_en_curso = get_object_or_404(MesEnCurso, pk=mes_en_curso_id)
    return render(request, 'registro_app/mes_en_curso/view.html', {'mes_en_curso': mes_en_curso, 'active_mes_en_cursos': True})


@login_required(login_url='/')
def mes_en_curso_delete(request, mes_en_curso_id):
    mes_en_curso = get_object_or_404(MesEnCurso, pk=mes_en_curso_id)
    if (request.method == 'POST'):
        mes_en_curso.delete()
    return redirect('mes_en_cursos')

# QSE


def qse_index(request):

    # qses = QSE.objects.all().order_by('nro')
    qses_filter = QSEFilter(
        request.GET, queryset=QSE.objects.all().order_by('nro'))
    paginator = Paginator(qses_filter.qs, 50)  # Show 50 per page.
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'registro_app/qse/index.html', {'qses': page_obj, 'qses_filter': qses_filter, 'active_qses': True})


@login_required(login_url='/')
def qse_new(request):
    if(request.method == 'GET'):
        return render(request, 'registro_app/qse/create.html', {'form': QSEForm(), 'active_qses': True})
    else:
        qse = QSEForm(request.POST)
        if qse.is_valid():
            qses = QSE.objects.order_by('-nro')
            try:
                nro = qses[0].nro + 1
            except:
                nro = 1
            newqse = qse.save(commit=False)
            newqse.nro = nro
            newqse.save()
            return redirect('qses')
        return render(request, 'registro_app/qse/create.html', {'form': qse, 'active_qses': True})


@login_required(login_url='/')
def qse_edit(request, qse_id):
    qse = get_object_or_404(QSE, pk=qse_id)

    if(request.method == 'GET'):
        form = QSEForm(instance=qse)
        return render(request, 'registro_app/qse/edit.html', {'form': form, 'active_qses': True})
    else:
        form = QSEForm(request.POST, instance=qse)
        if form.is_valid():
            form.save()
            return redirect('qse_view', qse.id)
        return render(request, 'registro_app/qse/edit.html', {'form': form, 'active_qses': True})


def qse_view(request, qse_id):
    qse = get_object_or_404(QSE, pk=qse_id)
    return render(request, 'registro_app/qse/view.html', {'qse': qse, 'active_qses': True})


@login_required(login_url='/')
def qse_delete(request, qse_id):
    qse = get_object_or_404(QSE, pk=qse_id)
    if (request.method == 'POST'):
        qse.delete()
    return redirect('qses')

# Subir un excel


@login_required(login_url='/')
def handle_uploaded_file(request, f, obra):
    with open('name.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        # try:
        wb = load_workbook(filename='name.xlsx')
        sheet_ranges = wb['Hoja1']
        if sheet_ranges['A2'].value == 'codigoConvenio' and sheet_ranges['B2'].value == 'descripcionConvenio':
            pos = 3
            obra = Obra.objects.get(pk=obra)
            convenios_list = []
            while (sheet_ranges['A' + str(pos)].value != None):
                convenios_list.append(Convenio(obra=obra,
                                               codigo=sheet_ranges['A' +
                                                                   str(pos)].value,
                                               descripcion=sheet_ranges['B'+str(pos)].value))
                # convenio_temp = Convenio(obra=obra,
                #                          codigo=sheet_ranges['A' +
                #                                              str(pos)].value,
                #                          descripcion=sheet_ranges['B'+str(pos)].value)
                pos += 1

            convenios = Convenio.objects.bulk_create(
                convenios_list, ignore_conflicts=True)
            # try:

            #     convenio_temp.save()
            # except IntegrityError:
            #     pass

            return True
        else:
            return False

        # except:
        #     return False


@login_required(login_url='/')
def upload_excel(request):
    if request.method == 'GET':
        form = UploadExcelForm()
        return render(request, 'registro_app/convenio/uploadExcel.html', {'form': form, 'success': False})
    else:
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            if handle_uploaded_file(request, request.FILES['archivo'], request.POST['obra']):
                return render(request, 'registro_app/convenio/uploadExcel.html', {'success': True})

        return render(request, 'registro_app/convenio/uploadExcel.html', {'error': True})
