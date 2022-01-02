from django import forms
from django.forms import ModelForm
from .models import Comment, Producto, Categoria, Contatecno


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = {'contenido', 'ranking'}

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = {'nombre', 'image', 'slug'}
        labels = {'nombre':'Nombre', 'image':'Imagen', 'slug':'Slug'}
class ProductForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'name', 
            'descripcion', 
            
            'price', 
            'image', 
            'categoria',
            'slug',
        ]
        labels = {
            'name': 'Nombre',
            'descripcion': 'Descripcion',
            
            'price': 'Precio',
            'image': 'Imagen',
            'categoria': 'Categoria',
            'slug':'Slug'
        }
class ContactoForm(ModelForm):
    class Meta:
        model = Contatecno
        fields = [
            'nombre', 
            'asunto', 
            'correo', 
            'mensaje',
            'telefono'
        ]
        labels = {
            'nombre': 'Nombre',
            'asunto': 'Asunto',
            'correo': 'Correo',
            'mensaje': 'Mensaje',
            'telefono': 'Telefono',
        }
class SearchForm(ModelForm):
    query = forms.CharField()