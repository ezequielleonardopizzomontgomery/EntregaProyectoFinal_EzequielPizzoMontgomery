from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registro/',views.registrarse, name='registrarse')
]
    
 