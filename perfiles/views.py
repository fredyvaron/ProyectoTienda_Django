from django.db.models.query import prefetch_related_objects
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import PerfilUsuario
from .forms import PerfilForm
from django.contrib.auth.models import User

# Create your views here.
def Perfil(request):
    url = request.META.get('HTTP_REFERER')
    template_name= "perfil/perfil.html"
    id_usua = request.user.id
    print(id_usua)
    id_perfil = PerfilUsuario.objects.get(usuario=id_usua)
    print(id_perfil)
    perfil = PerfilForm()
    if request.method == 'POST':
        perfil = PerfilForm(request.POST, request.FILES, instance=id_perfil)
        if perfil.is_valid():
            perfil.save()
        return HttpResponseRedirect(url)
    context={
         'form':perfil,
         'perfil':id_perfil
    }  
    return render(request,template_name,context )