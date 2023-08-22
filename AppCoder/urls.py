from django.urls import path
from . import views

urlpatterns = [
    path("" , views.inicio , name="Home"),
    path("ver_cursos" , views.ver_cursos),
    #path("alta_curso/<str:nombre>/<int:comision>" , views.alta_cursos),
    path("profesores" , views.profesores , name="profesores"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("alta_cursos", views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),
]