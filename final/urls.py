from django.contrib import admin
from django.urls import path
from clinica import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    #URLS Administradores
    path('admin/', admin.site.urls),
    path('ssstafff', views.staffmenu, name='staffmenu' ),
    path('pacientes', views.pacientes, name='pacientes'),
    path('pacientes/guardar', views.pacientesguardar, name='pacientesguardar'),
    path('pacientes/eliminar/<int:id>', views.pacienteseliminar, name='pacienteseliminar'),
    path('pacientes/mostrar/<int:id>', views.pacientesmostrar, name='pacientesmostrar'),
    path('pacientes/modificar', views.pacientesmodificar, name='pacientesmodificar'),
    path('medicos', views.medicos, name='medicos'),
    path('medicos/guardar', views.medicosguardar, name='medicosguardar'),
    path('medicos/eliminar/<int:id>', views.medicoseliminar, name='medicoseliminar'),
    path('medicos/mostrar/<int:id>', views.medicosmostrar, name='medicosmostrar'),
    path('medicos/modificar', views.medicosmodificar, name='medicosmodificar'),
    path('ssstafff/buzon', views.staffbuzon, name='staffbuzon'),
    path('ssstafff/citas', views.staffcitas, name='staffcitas'),
    path('ssstafff/citas/guardar', views.staffcitasguardar, name='staffcitasguardar'),
    path('ssstafff/citas/eliminar/<int:id>', views.staffcitaseliminar, name='staffcitaseliminar'),
    path('ssstafff/citas/mostrar/<int:id>', views.staffcitasmostrar, name='staffcitasmostrar'),
    path('ssstafff/citas/modificar', views.staffcitasmodificar, name='staffcitasmodificar'),
    #URLS Usuarios
    path('user', views.usuariomenu, name='usuariomenu'),
    path('user/registro', views.usuarioregistro, name='usuarioregistro'),
    path('user/registro/guardar', views.usuarioregistrar, name='usuarioregistrar'),
    path('user/mensaje',views.usuariomensaje,name='usuariomensaje'),
    path('user/mensaje/guardar',views.usuarioenviarmensaje,name='usuarioenviarmensaje'),
    path('user/cita', views.usuariocita, name='usuariocita'),
    path('user/cita/guardar', views.usuariocitaguardar, name='usuariocitaguardar'),
    #contra
    path('ingresar', views.ingresar, name='ingresar'),
    path('ingresar/verificar', views.verificar, name='verificar'),
]
