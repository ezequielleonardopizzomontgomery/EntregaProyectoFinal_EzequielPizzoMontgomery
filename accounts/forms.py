from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class MiFormularioDeCreacionDeUsuarios(UserCreationForm):
    first_name=forms.CharField(label='Nombre',max_length=20)
    last_name =forms.CharField(label='Apellido',max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    descripcion = forms.CharField(label='Descripcion',max_length=50)
    link = forms.CharField(label='Ruta',max_length=50)
    avatar = forms.ImageField(required=False) 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name','descripcion','link','avatar']
        help_texts = {k:"" for k in fields}
        
class MiFormularioDeEdicionDeDatosDelUsuario(UserChangeForm):
    password=None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre',max_length=20)
    last_name = forms.CharField(label='Apellido',max_length=20)
    descripcion = forms.CharField(label='Descripcion',max_length=50)
    link = forms.CharField(label='Ruta',max_length=50)
    avatar = forms.ImageField(required=False)
    
    class Meta():
        model=User
        fields=['email','first_name','last_name','descripcion','link','avatar']