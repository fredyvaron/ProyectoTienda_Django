from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import PerfilUsuario

class PerfilForm(ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = {'avatar', 'telefono', 'fecha_cumpleaños', 'genero' }
        labels = {'avatar':'Avatar', 'telefono':'Telefono', 'fecha_cumpleaños':'Fecha De Cumpleaños', 'genero':'Genero' }
        widgets = {'fecha_cumpleaños':forms.DateInput(attrs={'type': 'date'})}