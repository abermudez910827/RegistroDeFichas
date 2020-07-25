from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login as v_login,logout as v_logout

def index(request):
    return render(request, 'registro_app/index.html')
    

def signupuser(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm})
    else:
        #Creacion de usuario
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                v_login(request,user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm,'error':'El usuario ya existe'})

        else:
            #Contrasena no coincide
            return render(request, 'registro_app/singupuser.html', {'form': UserCreationForm,'error':'Las contraseñas no coinciden'})
            
def logout(request):
    if request.method == 'POST':
        v_logout(request)
        return redirect('index')


def login(request):
    if(request.method=='GET'):
        return render(request, 'registro_app/login.html',{'form':AuthenticationForm()})
    else:
        #Login de usuario
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'registro_app/login.html', {'form': AuthenticationForm(), 'error': 'Usuario o contraseña incorrecta'})
        else:
            v_login(request, user)
            return redirect('index')



    
