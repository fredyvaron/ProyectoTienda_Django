from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# Create your models here.
FAVORITES_CHOICES = (
	('U', 'Up Vote'),
	('D', 'Down Vote'),
)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categorias/', default='products/default.png')
    slug = models.SlugField(max_length=255, unique=True)
    def get_absolute_url(self):
        return reverse('tienda:categoria_lista', args=[self.slug])
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.TextField()
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=30,decimal_places=1)
    image = models.ImageField(upload_to='products/', default='products/default.png')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE , related_name='productos')
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-creado']

    def get_absolute_url(self):
        return reverse('tienda:producto_detail', args=[self.slug])
    def __str__(self):
        return self.name
class Comment(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ranking = models.IntegerField(default=1)
    contenido = models.TextField()
    favoritos = models.IntegerField(default=0)
    creado = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.contenido

    def calcular_favoritos(self):
        u_favoritos = Favoritos.objects.filter(comentario=self, favorito='U').count()
        d_favoritos = Favoritos.objects.filter(comentario=self, favorito='D').count()
        self.favoritos = u_favoritos-d_favoritos
        self.save()
        return self.favoritos
class Favoritos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos_user')
    comentario = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comentario_favoritos')
    favorito = models.CharField(choices=FAVORITES_CHOICES, max_length=1)
    date = models.DateTimeField(auto_now_add=True)

class Contatecno(models.Model):
    nombre = models.CharField(max_length=70)
    asunto = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    mensaje = models.TextField()
    telefono = models.CharField(max_length=20)


    def __str__(self):
        return self.nombre

# UpVotes
class UpVote(models.Model):
    comentario=models.ForeignKey(Comment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='upvote_user')

# DownVotes
class DownVote(models.Model):
    comentario=models.ForeignKey(Comment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='downvote_user')