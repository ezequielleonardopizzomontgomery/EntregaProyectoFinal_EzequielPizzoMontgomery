from django.urls import path
from accounts import views 
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from django.views.generic import TemplateView



app_name = 'accounts'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('informacion_pagina', views.inicio, name='informacion_pagina'),
    path('registro/',views.registrarse, name='registrarse'),
    path('perfil/editar/', views.edicion_perfil, name='edicion_perfil'),
    path('perfil/editar/password', views.ModificarPass.as_view(), name='modificar_pass'),
]
    
urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='accounts/errores_ruta.html'), name='errores_ruta'),
]

