from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),#si no te llega nada, redirigi a lo que esta en "include(aplicacion.urls)"
]
