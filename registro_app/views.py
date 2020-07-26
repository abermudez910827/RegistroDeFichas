from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login as v_login,logout as v_logout
from .forms import PersonaForm,EspecialidadForm,ActividadForm,ObraForm
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
   
def persona_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/persona/create.html', {'form': PersonaForm(),'active_datos':True})
    else:           
        persona = PersonaForm(request.POST)
        if persona.is_valid():
            persona.save()
            return redirect('personas')
        return render(request, 'registro_app/persona/create.html', {'form': persona,'active_datos':True})

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
 
def persona_delete(request,persona_id):
        persona = get_object_or_404(Persona, pk=persona_id)
        if (request.method == 'POST'):
            persona.delete()
        return redirect('personas')
 
 #Especialidades

def especialidad_index(request):
        especialidades= Especialidad.objects.all()
        return render(request, 'registro_app/especialidad/index.html',{'especialidades':especialidades,'active_datos':True})
   
def especialidad_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/especialidad/create.html', {'form': EspecialidadForm(),'active_datos':True})
    else:           
        especialidad = EspecialidadForm(request.POST)
        if especialidad.is_valid():
            especialidad.save()
            return redirect('especialidades')
        return render(request, 'registro_app/especialidad/create.html', {'form': especialidad,'active_datos':True})

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
 
def especialidad_delete(request,especialidad_id):
        especialidad = get_object_or_404(Especialidad, pk=especialidad_id)
        if (request.method == 'POST'):
            especialidad.delete()
        return redirect('especialidades')

#actividades

def actividad_index(request):
        actividades= Actividad.objects.all()
        return render(request, 'registro_app/actividad/index.html',{'actividades':actividades,'active_datos':True})
   
def actividad_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/actividad/create.html', {'form': ActividadForm(),'active_datos':True})
    else:           
        actividad = ActividadForm(request.POST)
        if actividad.is_valid():
            actividad.save()
            return redirect('actividades')
        return render(request, 'registro_app/actividad/create.html', {'form': actividad,'active_datos':True})

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
 
def actividad_delete(request,actividad_id):
        actividad = get_object_or_404(Actividad, pk=actividad_id)
        if (request.method == 'POST'):
            actividad.delete()
        return redirect('actividades')
 
#Obras
def obra_index(request):
        obras= Obra.objects.all()
        return render(request, 'registro_app/obra/index.html',{'obras':obras,'active_obras':True})
   
def obra_new(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/obra/create.html', {'form': ObraForm(),'active_obras':True})
    else:           
        obra = ObraForm(request.POST)
        if obra.is_valid():
            obra.save()
            return redirect('obras')
        return render(request, 'registro_app/obra/create.html', {'form': obra,'active_obras':True})

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
 
def obra_delete(request,obra_id):
        obra = get_object_or_404(Obra, pk=obra_id)
        if (request.method == 'POST'):
            obra.delete()
        return redirect('obras')
 

 