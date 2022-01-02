from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date
# Create your models here.
GENDER = (('hombre', 'Hombre'), ('Mujer', 'Mujer'))
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='Media/perfiles_usuario/', default='images/default.png')
    telefono = models.CharField(max_length=20)
    fecha_cumpleaños = models.DateField(default=date.today)
    genero = models.CharField(max_length=40, blank=True, verbose_name=('Gender'), choices=GENDER)
    completo = models.BooleanField(default=False)
    def __str__(self):
        return self.usuario.username

def create_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)
post_save.connect(create_perfil, sender=User)