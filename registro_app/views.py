from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login as v_login,logout as v_logout
from .forms import PersonaForm,EspecialidadForm,ActividadForm,ObraForm,BrigadaForm,ObjetoForm,ZonaForm,ConvenioForm
from .models import Persona,Convenio,Especialidad,Brigada,QSE,Actividad,Zona,Objeto,Obra,MesEnCurso

def index(request):
    return render(request, 'registro_app/index.html',{'active_index':True})
    

def signupuser(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm,'active_signup':True})
    else:
        #Creacion de usuario
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                v_login(request,user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm,'error':'El usuario ya existe','active_signup':True})

        else:
            #Contrasena no coincide
            return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm,'error':'Las contraseñas no coinciden','active_signup':True})

def denegado(request):
        return render(request, 'registro_app/errors/505.html')
    
def logout(request):
    if request.method == 'POST':
        v_logout(request)
        return redirect('index')


def login(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/index.html',{'form':AuthenticationForm(),'active_index':True})
    else:
        #Login de usuario
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'registro_app/index.html', {'form': AuthenticationForm(), 'error': 'Usuario o contraseña incorrecta','active_index':True})
        else:
            v_login(request, user)
            return redirect('index')

def persona_index(request):
        personas= Persona.objects.all()
        return render(request, 'registro_app/persona/index.html',{'personas':personas,'active_datos':True})
   
@login_required(login_url='/')
def persona_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/persona/create.html', {'form': PersonaForm(),'active_datos':True})
    else:           
        persona = PersonaForm(request.POST)
        if persona.is_valid():
            persona.save()
            return redirect('personas')
        return render(request, 'registro_app/persona/create.html', {'form': persona,'active_datos':True})
@login_required(login_url='/')
def persona_edit(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    
    if(request.method=='GET'):
        form=PersonaForm(instance=persona)
        return render(request, 'registro_app/persona/create.html',{'form': form,'active_datos':True})
    else:        
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona_view',persona.id)
        return render(request, 'registro_app/persona/create.html', {'form': form,'active_datos':True})

def persona_view(request,persona_id):
    persona= get_object_or_404(Persona,pk=persona_id)
    return render(request, 'registro_app/persona/view.html',{'persona':persona,'active_datos':True})
@login_required(login_url='/')
def persona_delete(request,persona_id):
        persona = get_object_or_404(Persona, pk=persona_id)
        if (request.method == 'POST'):
            persona.delete()
        return redirect('personas')
 
 #Especialidades

def especialidad_index(request):
        especialidades= Especialidad.objects.all()
        return render(request, 'registro_app/especialidad/index.html',{'especialidades':especialidades,'active_datos':True})
@login_required(login_url='/')
def especialidad_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/especialidad/create.html', {'form': EspecialidadForm(),'active_datos':True})
    else:           
        especialidad = EspecialidadForm(request.POST)
        if especialidad.is_valid():
            especialidad.save()
            return redirect('especialidades')
        return render(request, 'registro_app/especialidad/create.html', {'form': especialidad,'active_datos':True})
@login_required(login_url='/')
def especialidad_edit(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, pk=especialidad_id)
    
    if(request.method=='GET'):
        form=EspecialidadForm(instance=especialidad)
        return render(request, 'registro_app/especialidad/create.html',{'form': form,'active_datos':True})
    else:        
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('especialidad_view',especialidad.id)
        return render(request, 'registro_app/especialidad/create.html', {'form': form,'active_datos':True})
  
def especialidad_view(request,especialidad_id):
        especialidad= get_object_or_404(Especialidad,pk=especialidad_id)
        return render(request, 'registro_app/especialidad/view.html',{'especialidad':especialidad,'active_datos':True})
@login_required(login_url='/')
def especialidad_delete(request,especialidad_id):
        especialidad = get_object_or_404(Especialidad, pk=especialidad_id)
        if (request.method == 'POST'):
            especialidad.delete()
        return redirect('especialidades')

#actividades

def actividad_index(request):
        actividades= Actividad.objects.all()
        return render(request, 'registro_app/actividad/index.html',{'actividades':actividades,'active_datos':True})
@login_required(login_url='/')
def actividad_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/actividad/create.html', {'form': ActividadForm(),'active_datos':True})
    else:           
        actividad = ActividadForm(request.POST)
        if actividad.is_valid():
            actividad.save()
            return redirect('actividades')
        return render(request, 'registro_app/actividad/create.html', {'form': actividad,'active_datos':True})
@login_required(login_url='/')
def actividad_edit(request, actividad_id):
    actividad = get_object_or_404(Actividad, pk=actividad_id)
    
    if(request.method=='GET'):
        form=ActividadForm(instance=actividad)
        return render(request, 'registro_app/actividad/create.html',{'form': form,'active_datos':True})
    else:        
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividad_view',actividad.id)
        return render(request, 'registro_app/actividad/create.html', {'form': form,'active_datos':True})
  
def actividad_view(request,actividad_id):
        actividad= get_object_or_404(Actividad,pk=actividad_id)
        return render(request, 'registro_app/actividad/view.html',{'actividad':actividad,'active_datos':True})
@login_required(login_url='/')
def actividad_delete(request,actividad_id):
        actividad = get_object_or_404(Actividad, pk=actividad_id)
        if (request.method == 'POST'):
            actividad.delete()
        return redirect('actividades')
 
#Obras
def obra_index(request):
        obras= Obra.objects.all()
        return render(request, 'registro_app/obra/index.html',{'obras':obras,'active_obras':True})
@login_required(login_url='/')
def obra_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/obra/create.html', {'form': ObraForm(),'active_obras':True})
    else:           
        obra = ObraForm(request.POST)
        if obra.is_valid():
            obra.save()
            return redirect('obras')
        return render(request, 'registro_app/obra/create.html', {'form': obra,'active_obras':True})
@login_required(login_url='/')
def obra_edit(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    
    if(request.method=='GET'):
        form=ObraForm(instance=obra)
        return render(request, 'registro_app/obra/create.html',{'form': form,'active_obras':True})
    else:        
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('obra_view',obra.id)
        return render(request, 'registro_app/obra/create.html', {'form': form,'active_obras':True})
  
def obra_view(request,obra_id):
        obra= get_object_or_404(Obra,pk=obra_id)
        return render(request, 'registro_app/obra/view.html',{'obra':obra,'active_obras':True})
@login_required(login_url='/')
def obra_delete(request,obra_id):
        obra = get_object_or_404(Obra, pk=obra_id)
        if (request.method == 'POST'):
            obra.delete()
        return redirect('obras')
 
#Objetos
def objeto_index(request):
        objetos= Objeto.objects.all()
        return render(request, 'registro_app/objeto/index.html', {'objetos': objetos, 'active_objetos': True})
        
@login_required(login_url='/')
def objeto_new(request):
        if(request.method=='GET'):
            return render(request, 'registro_app/objeto/create.html', {'form': ObjetoForm(),'active_objetos':True})
        else:           
            objeto = ObjetoForm(request.POST)
            if objeto.is_valid():
                objeto.save()
                return redirect('objetos')
            return render(request, 'registro_app/objeto/create.html', {'form': objeto, 'active_objetos': True})
    

@login_required(login_url='/')
def objeto_edit(request, objeto_id):
        objeto = get_object_or_404(Objeto, pk=objeto_id)
        
        if(request.method=='GET'):
            form=ObjetoForm(instance=objeto)
            return render(request, 'registro_app/objeto/create.html',{'form': form,'active_objetos':True})
        else:        
            form = ObjetoForm(request.POST, instance=objeto)
            if form.is_valid():
                form.save()
                return redirect('objeto_view',objeto.id)
            return render(request, 'registro_app/objeto/create.html', {'form': form,'active_objetos':True})
    
def objeto_view(request,objeto_id):
        objeto= get_object_or_404(Objeto,pk=objeto_id)
        return render(request, 'registro_app/objeto/view.html', {'objeto': objeto, 'active_objetos': True})
        
@login_required(login_url='/')
def objeto_delete(request,objeto_id):
        objeto = get_object_or_404(Objeto, pk=objeto_id)
        if (request.method == 'POST'):
            objeto.delete()
        return redirect('objetos')
   
#Zonas
def zona_index(request):
        zonas= Zona.objects.all()
        return render(request, 'registro_app/zona/index.html', {'zonas': zonas, 'active_zonas': True})
        
@login_required(login_url='/')
def zona_new(request):
        if(request.method=='GET'):
            return render(request, 'registro_app/zona/create.html', {'form': ZonaForm(),'active_zonas':True})
        else:           
            zona = ZonaForm(request.POST)
            if zona.is_valid():
                zona.save()
                return redirect('zonas')
            return render(request, 'registro_app/zona/create.html', {'form': zona, 'active_zonas': True})
   

@login_required(login_url='/')
def zona_edit(request, zona_id):
        zona = get_object_or_404(Zona, pk=zona_id)
        
        if(request.method=='GET'):
            form=ZonaForm(instance=zona)
            return render(request, 'registro_app/zona/create.html',{'form': form,'active_zonas':True})
        else:        
            form = ZonaForm(request.POST, instance=zona)
            if form.is_valid():
                form.save()
                return redirect('zona_view',zona.id)
            return render(request, 'registro_app/zona/create.html', {'form': form,'active_zonas':True})
    
def zona_view(request,zona_id):
        zona= get_object_or_404(Zona,pk=zona_id)
        return render(request, 'registro_app/zona/view.html', {'zona': zona, 'active_zonas': True})
        
@login_required(login_url='/')
def zona_delete(request,zona_id):
        zona = get_object_or_404(Zona, pk=zona_id)
        if (request.method == 'POST'):
            zona.delete()
        return redirect('zonas')
   
#Brigadas
def brigada_index(request):
        brigadas= Brigada.objects.all()
        return render(request, 'registro_app/brigada/index.html', {'brigadas': brigadas, 'active_brigadas': True})
        
@login_required(login_url='/')
def brigada_new(request):
        if(request.method=='GET'):
            return render(request, 'registro_app/brigada/create.html', {'form': BrigadaForm(),'active_brigadas':True})
        else:           
            brigada = BrigadaForm(request.POST)
            if brigada.is_valid():
                brigada.save()
                return redirect('brigadas')
            return render(request, 'registro_app/brigada/create.html', {'form': brigada, 'active_brigadas': True})
   

@login_required(login_url='/')
def brigada_edit(request, brigada_id):
        brigada = get_object_or_404(Brigada, pk=brigada_id)
        
        if(request.method=='GET'):
            form=BrigadaForm(instance=brigada)
            return render(request, 'registro_app/brigada/create.html',{'form': form,'active_brigadas':True})
        else:        
            form = BrigadaForm(request.POST, instance=brigada)
            if form.is_valid():
                form.save()
                return redirect('brigada_view',brigada.id)
            return render(request, 'registro_app/brigada/create.html', {'form': form,'active_brigadas':True})
    
def brigada_view(request,brigada_id):
        brigada= get_object_or_404(Brigada,pk=brigada_id)
        return render(request, 'registro_app/brigada/view.html', {'brigada': brigada, 'active_brigadas': True})
        
@login_required(login_url='/')
def brigada_delete(request,brigada_id):
    brigada = get_object_or_404(Brigada, pk=brigada_id)
    if (request.method == 'POST'):
        brigada.delete()
    return redirect('brigadas')
   
#Convenios
def convenio_index(request):
    convenios= Convenio.objects.all()
    return render(request, 'registro_app/convenio/index.html', {'convenios': convenios, 'active_convenios': True})
        
@login_required(login_url='/')
def convenio_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/convenio/create.html', {'form': ConvenioForm(),'active_convenios':True})
    else:           
        convenio = ConvenioForm(request.POST)
        if convenio.is_valid():
            convenio.save()
            return redirect('convenios')
        return render(request, 'registro_app/convenio/create.html', {'form': convenio, 'active_convenios': True})
   

@login_required(login_url='/')
def convenio_edit(request, convenio_id):
        convenio = get_object_or_404(Convenio, pk=convenio_id)
        
        if(request.method=='GET'):
            form=ConvenioForm(instance=convenio)
            return render(request, 'registro_app/convenio/create.html',{'form': form,'active_convenios':True})
        else:        
            form = ConvenioForm(request.POST, instance=convenio)
            if form.is_valid():
                form.save()
                return redirect('convenio_view',convenio.id)
            return render(request, 'registro_app/convenio/create.html', {'form': form,'active_convenios':True})
    
def convenio_view(request,convenio_id):
        convenio= get_object_or_404(Convenio,pk=convenio_id)
        return render(request, 'registro_app/convenio/view.html', {'convenio': convenio, 'active_convenios': True})
        
@login_required(login_url='/')
def convenio_delete(request,convenio_id):
        convenio = get_object_or_404(Convenio, pk=convenio_id)
        if (request.method == 'POST'):
            convenio.delete()
        return redirect('convenios')
