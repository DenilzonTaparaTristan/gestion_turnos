from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_paciente/', views.registrar_paciente, name='registrar_paciente'),
    path('asignar_turno/', views.asignar_turno, name='asignar_turno'),
    path('reprogramar_turno/', views.reprogramar_turno, name='reprogramar_turno'),
    path('generar_reportes/', views.generar_reportes, name='generar_reportes'),
    path('listar_turnos/', views.listar_turnos, name='listar_turnos'),
    path('reprogramar_turno/', views.reprogramar_turno, name='reprogramar_turno'),
    path('generar_reportes/', views.generar_reportes, name='generar_reportes'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
