from django.contrib import admin
from django.urls import path
from .views import register_request, logout_request, login_request, password_reset_request
app_name='users'
urlpatterns = [
    path('registro', register_request, name="registro_de_usuario"),
    path('logout', logout_request, name="logout_de_usuario"),
    path('login', login_request, name="login_de_usuario"),
    path("password_reset", password_reset_request, name="password_reset"),
]