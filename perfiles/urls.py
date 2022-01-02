from django.contrib import admin
from django.urls import path
from .views import Perfil
app_name='perfil'
urlpatterns = [
    path('perfil', Perfil, name="perfil_de_usuario"),
]
