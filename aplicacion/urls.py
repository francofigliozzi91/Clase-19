from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home, name="home" ), #Si no llega nada lo rediriga a la funcion home
    path('cursos/', cursos, name="cursos" ),
    path('profesores/', profesores, name="profesores" ),
    path('estudiantes/', estudiantes, name="estudiantes" ),
    path('entregables/', entregables, name="entregables" ),
]