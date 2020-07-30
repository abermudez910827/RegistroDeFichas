"""registro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from registro_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    # path('signup/', views.signupuser, name = 'registro'),
    path('logout/', views.logout, name = 'logout'),
    path('505/', views.denegado, name = 'denegado'),

    path('', views.login, name = 'login'),
    
    #registro_app
    path('', views.login, name = 'index'),
    #personas
    path('personas/', views.persona_index, name = 'personas'),
    path('personas/nueva', views.persona_new, name = 'persona_new'),
    path('personas/<int:persona_id>', views.persona_view, name = 'persona_view'),
    path('personas/edit/<int:persona_id>', views.persona_edit, name = 'persona_edit'),
    path('personas/delete/<int:persona_id>', views.persona_delete, name = 'persona_delete'),
    #Especialidades
    path('especialidades/', views.especialidad_index, name = 'especialidades'),
    path('especialidades/nueva', views.especialidad_new, name = 'especialidad_new'),
    path('especialidades/<int:especialidad_id>', views.especialidad_view, name = 'especialidad_view'),
    path('especialidades/edit/<int:especialidad_id>', views.especialidad_edit, name = 'especialidad_edit'),
    path('especialidades/delete/<int:especialidad_id>', views.especialidad_delete, name = 'especialidad_delete'),
    #Actividades
    path('actividades/', views.actividad_index, name = 'actividades'),
    path('actividades/nueva', views.actividad_new, name = 'actividad_new'),
    path('actividades/<int:actividad_id>', views.actividad_view, name = 'actividad_view'),
    path('actividades/edit/<int:actividad_id>', views.actividad_edit, name = 'actividad_edit'),
    path('actividades/delete/<int:actividad_id>', views.actividad_delete, name = 'actividad_delete'),
    #Obra
    path('obras/', views.obra_index, name = 'obras'),
    path('obras/nueva', views.obra_new, name = 'obra_new'),
    path('obras/<int:obra_id>', views.obra_view, name = 'obra_view'),
    path('obras/edit/<int:obra_id>', views.obra_edit, name = 'obra_edit'),
    path('obras/delete/<int:obra_id>', views.obra_delete, name = 'obra_delete'),
    #Objeto
    path('objetos/', views.objeto_index, name = 'objetos'),
    path('objetos/nueva', views.objeto_new, name = 'objeto_new'),
    path('objetos/<int:objeto_id>', views.objeto_view, name = 'objeto_view'),
    path('objetos/edit/<int:objeto_id>', views.objeto_edit, name = 'objeto_edit'),
    path('objetos/delete/<int:objeto_id>', views.objeto_delete, name = 'objeto_delete'),
    path('ajax/load-objetos/', views.load_objetos, name='ajax_load_objetos'),
    #Zona
    path('zonas/', views.zona_index, name = 'zonas'),
    path('zonas/nueva', views.zona_new, name = 'zona_new'),
    path('zonas/<int:zona_id>', views.zona_view, name = 'zona_view'),
    path('zonas/edit/<int:zona_id>', views.zona_edit, name = 'zona_edit'),
    path('zonas/delete/<int:zona_id>', views.zona_delete, name = 'zona_delete'),
    #Brigadas
    path('brigadas/', views.brigada_index, name = 'brigadas'),
    path('brigadas/nueva', views.brigada_new, name = 'brigada_new'),
    path('brigadas/<int:brigada_id>', views.brigada_view, name = 'brigada_view'),
    path('brigadas/edit/<int:brigada_id>', views.brigada_edit, name = 'brigada_edit'),
    path('brigadas/delete/<int:brigada_id>', views.brigada_delete, name = 'brigada_delete'),
    #Convenios
    path('convenios/', views.convenio_index, name = 'convenios'),
    path('convenios/nueva', views.convenio_new, name = 'convenio_new'),
    path('convenios/<int:convenio_id>', views.convenio_view, name = 'convenio_view'),
    path('convenios/edit/<int:convenio_id>', views.convenio_edit, name = 'convenio_edit'),
    path('convenios/delete/<int:convenio_id>', views.convenio_delete, name = 'convenio_delete'),
    #MesEnCurso
    path('mes_en_cursos/', views.mes_en_curso_index, name = 'mes_en_cursos'),
    path('mes_en_cursos/nueva', views.mes_en_curso_new, name = 'mes_en_curso_new'),
    path('mes_en_cursos/<int:mes_en_curso_id>', views.mes_en_curso_view, name = 'mes_en_curso_view'),
    path('mes_en_cursos/edit/<int:mes_en_curso_id>', views.mes_en_curso_edit, name = 'mes_en_curso_edit'),
    path('mes_en_cursos/delete/<int:mes_en_curso_id>', views.mes_en_curso_delete, name = 'mes_en_curso_delete'),
    #QSE
    path('qses/', views.qse_index, name = 'qses'),
    path('qses/nueva', views.qse_new, name = 'qse_new'),
    path('qses/<int:qse_id>', views.qse_view, name = 'qse_view'),
    path('qses/edit/<int:qse_id>', views.qse_edit, name = 'qse_edit'),
    path('qses/delete/<int:qse_id>', views.qse_delete, name = 'qse_delete'),
    

]

