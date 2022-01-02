from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
@login_required(login_url="users:login_de_usuario")
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
@login_required(login_url="users:login_de_usuario")
def add_cart(request, product_id):
    user = request.user
    product = Producto.objects.get(id=product_id)
    if user.is_authenticated:
        if CartItem.objects.filter(product=product, user = user).exists():
            cart_item = CartItem.objects.get(product=product, user = user)
            cart_item.quantity +=1
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            user = user,
        )
            cart_item.save()
    
        return redirect("carro:cart_detail")

    else:

        product = Producto.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart.save()
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
            cart.save()

        try:
            cart_item =CartItem.objects.get(product=product, cart = cart)
            cart_item.quantity +=1
            cart_item.save()
            
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
            )
            cart_item.save()
    
        return redirect("carro:cart_detail")
@login_required(login_url="users:login_de_usuario")
def remove_cart(request, product_id):
    user = request.user
    if user.is_authenticated:
        product = get_object_or_404(Producto, id=product_id)
        if CartItem.objects.filter(user=user, product=product).exists():
            cart_item = CartItem.objects.get(user=user, product=product)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        return redirect("carro:cart_detail")
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Producto, id=product_id)
        cart_item = CartItem.objects.get(cart=cart, product=product)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
            
        return redirect("carro:cart_detail")

@login_required(login_url="users:login_de_usuario")
def remove_cart1(request):
    user = request.user
    if user.is_authenticated:
        cart_items = CartItem.objects.filter(user=user)
        for Data in cart_items:
            Data.delete()
        return redirect("carro:cart_detail")
    else:
        carts = Cart.objects.filter(cart_id=_cart_id(request))
        for Datas in carts:
            Datas.delete()
        return redirect("carro:cart_detail")


@login_required(login_url="users:login_de_usuario")
def remove_cart_item(request, product_id):
    user = request.user
    if user.is_authenticated:
        product = get_object_or_404(Producto, id=product_id)
        if CartItem.objects.filter(user=user, product=product).exists():
            cart_item = CartItem.objects.get(user=user, product=product)
            cart_item.delete()
        return redirect("carro:cart_detail")
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Producto, id=product_id)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
        return redirect("carro:cart_detail")
@login_required(login_url="users:login_de_usuario")
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for item in cart_items:
            #if item.product.discount_price:
            #    total += round((item.product.discount_price * item.quantity), 2)
            #    quantity += item.quantity
            #else:
            total += round((item.product.price * item.quantity), 2)
            quantity += item.quantity

        tax = round(((2 * total) / 100), 2)
        grand_total = round((tax + total), 2) 

    except ObjectDoesNotExist:
        pass

    context = {
            'total':total,
            'quantity':quantity,
            'cart_items':cart_items,
            'tax':tax,
            'grand_total':grand_total,
        }

    return render(request, 'carro/suma.html', context)



