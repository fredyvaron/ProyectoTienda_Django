from django.contrib import admin
from django.urls import path
from .views import add_cart, remove_cart, cart, remove_cart_item, remove_cart1
#from .views import Index, Producto_detail, Lista_categoria

app_name = 'carro'
urlpatterns = [
    path('cart/add/<int:product_id>/', add_cart, name='cart_add'),
    path('cart/item_clear/<int:product_id>/', remove_cart, name='item_clear'),
    path('cart/cart-detail/', cart,name='cart_detail'),

    #path('cart/item_increment/<int:id>/', item_increment, name='item_increment'),
    #path('cart/item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart/cart_clear/', remove_cart1, name='cart_clear'),
    
]