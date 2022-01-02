from django.contrib import admin
from django.urls import path
from .views import Index, Producto_detail, Lista_categoria, Crear_producto,Producto_new, Categoria_new, Contactenos, Detalle_categoria, Agregar_comentario, like_producto, save_upvote, save_downvote
from django.conf import settings
from django.conf.urls.static import static

app_name = 'producto'
urlpatterns = [
    path('', Index, name='producto_home'),
    path('<slug:slug>', Producto_detail, name='producto_detail'),
    path('producto/<slug:categoria_slug>/', Lista_categoria, name='categoria_lista'),
    path('crearproducto/', Crear_producto, name='crear_producto'),
    path('productonew/', Producto_new, name='new_producto'),
    path('categoria/', Categoria_new, name='new_categoria'),
    path('contactenos/', Contactenos, name='contactenos'),
    path('detallecategoria/<int:categoria_id>', Detalle_categoria, name='detalle_categoria'),
    path('addcoment/<int:id>/', Agregar_comentario, name='agregar_comentario' ),
    path('like/', like_producto, name='product_like'),
    path('save-upvotes',save_upvote,name='save-upvotes'),
    path('save-downvote',save_downvote,name='save-downvote'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

