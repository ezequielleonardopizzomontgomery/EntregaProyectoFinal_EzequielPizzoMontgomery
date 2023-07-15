from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from accounts.forms import MiFormularioDeCreacionDeUsuarios, MiFormularioDeEdicionDeDatosDelUsuario
from django.urls import reverse_lazy
from accounts.models import InfoExtra

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            return render(request, 'accounts/login.html', {'formulario':formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'accounts/login.html', {'formulario':formulario})


def registrarse(request):
    if request.method == 'POST':
        formulario =MiFormularioDeCreacionDeUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ('accounts:login')
        else:
            return render(request , 'accounts/registro.html', {'formulario':formulario})
    
    formulario = MiFormularioDeCreacionDeUsuarios()
    return render(request , 'accounts/registro.html', {'formulario':formulario})

@login_required
def edicion_perfil(request):
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDeDatosDelUsuario(request.POST, request.FILES,instance=request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()
            
            formulario.save()
            return redirect('inicio:inicio')
    else:
        formulario = MiFormularioDeEdicionDeDatosDelUsuario(initial={'avatar':info_extra_user.avatar},instance=request.user)
        
    return render (request, 'accounts/edicion_perfil.html',{'formulario': formulario})
    ##formulario = MiFormularioDeCreacionDeUsuarios(instance=request.user)
    ##return render(request, 'accounts/edicion_perfil.html', {'formulario':formulario})