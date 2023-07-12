from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'accounts/login.html', {'formulario':formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'accounts/login.html', {'formulario':formulario})
