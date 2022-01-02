from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models.aggregates import Avg, Sum
from .models import Producto, Categoria, Comment
from .forms import CategoriaForm, CommentForm, ProductForm, ContactoForm

# Create your views here.
def Index(request):
    template_name= "productos/index.html"
    #productos=Producto.objects.all()
    productos = Producto.objects.annotate(ranking=Avg('comment__ranking'))
    context={
        'productos': productos
    }
    return render(request, template_name, context)
def Detalle_categoria(request, categoria_id):
    template_name = "productos/detalle_categoria.html"
    categoria = get_object_or_404(Categoria, id=categoria_id)
    producto = Producto.objects.filter(categoria=categoria)
    context = {
        'categoria': categoria,
        'productos': producto
    }
    return render(request, template_name, context)
def Lista_categoria(request, category_slug=None):
    category = get_object_or_404(Categoria, slug=category_slug)
    products = Producto.products.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def Producto_detail(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    response_data = {}
    is_liked = False

    reviewse = Comment.objects.filter(producto=producto)

    answers_list = list(reviewse)

    review_avg = reviewse.aggregate(Avg('ranking'))
    review_one = Comment.objects.filter(ranking="1", producto=producto)
    review_two = Comment.objects.filter(ranking="2", producto=producto)
    review_three = Comment.objects.filter(ranking="3", producto=producto)
    review_four = Comment.objects.filter(ranking="4", producto=producto)
    review_five = Comment.objects.filter(ranking="5", producto=producto)
    context = {
        'producto': producto,
        'review': reviewse,
        'review_con': review_avg,
        'review_one': review_one,
        'review_two': review_two,
        'review_three': review_three,
        'review_four': review_four,
        'review_five': review_five,
        'is_liked': is_liked,


    }
    if request.method == 'POST' and request.user.is_authenticated:
        contenido = request.POST.get('contenido')
        ranking = request.POST.get('ranking')
        response_data['contenido'] = contenido
        response_data['ranking'] = ranking
        review = Comment.objects.create(
            producto=producto, user=request.user, contenido=contenido, ranking=ranking)
        return JsonResponse(response_data)
    else:
        review = CommentForm()

    return render(request, 'productos/detalle.html', context)
def Contactenos(request):
    url = request.META.get('HTTP_REFERER')
    template_name = "productos/contactenos.html"
    contacto = ContactoForm()
    if request.method == 'POST':
        contacto = ContactoForm(request.POST, request.FILES)
        if contacto.is_valid():
            contacto.save()
        return HttpResponseRedirect(url)
    context = {
        'form': contacto,
    }
    return render(request, template_name, context)


def Categoria_new(request):
    url = request.META.get('HTTP_REFERER')
    template_name = "productos/categoria_new.html"
    categorias = Categoria.objects.all()
    categoria = CategoriaForm()
    if request.method == 'POST':
        categoria = CategoriaForm(request.POST, request.FILES)
        if categoria.is_valid():
            data = Categoria()
            data.nombre = categoria.cleaned_data['nombre']
            data.image = categoria.cleaned_data['image']
            data.slug = categoria.cleaned_data['slug']
            data.save()
        return HttpResponseRedirect(url)
    context = {
        'form': categoria,
        'categoria': categorias
    }
    return render(request, template_name, context)


def Producto_new(request):
    messages = {}
    producto = ProductForm(request.POST, request.FILES)
    if producto.is_valid():
        producto.save()

        producto = ProductForm
    else:
        messages = 'error'
        return render(request, 'productos/crear_producto.html', {'form': producto, 'err': messages})
    return redirect("producto:producto_home")


def Crear_producto(request):
    form = ProductForm()
    return render(request, 'productos/crear_producto.html', {'form': form})


def FavoritoAdd(request):
    user = request.user
    commentario_id = request.POST['comentario_id']
    favorite_type = request.POST['vote_type']
    try:
        comentario = get_object_or_404(Comment, id=commentario_id)
        favorites = Favoritos.objects.filter(
            user=user, comentario=commentario_id)
        if favorites:
            favorites.delete()
        else:
            if favorite_type == 'U':
                Favoritos.objects.create(
                    user=user, answer=comentario, vote='U')
            else:
                Favoritos.objects.create(
                    user=user, answer=comentario, vote='D')
            return HttpResponse(comentario.calcular_favoritos())
    except Exception as e:
        raise e


def like_producto(request):
    producto = get_object_or_404(Producto, id=request.POST.get('product_id'))
    is_liked = False
    if producto.likes.filter(id=request.user.id).exists():
        producto.likes.remove(request.user)
        is_liked = False
    else:
        producto.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(producto.get_absolute_url())


def Agregar_comentario(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.contenido = form.cleaned_data['contenido']
            #data.ranking = form.cleaned_data['ranking']
            data.producto = id
            data.ranking = 1
            current_user = request.user
            data.user = 1
            data.save()
            messages.success(request, "Su Review Su Enviada")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

# Save Upvote


def save_upvote(request):
    if request.method == 'POST':
        comentarioid = request.POST['comentarioid']
        comentario = Comment.objects.get(pk=comentarioid)
        user = request.user
        check = UpVote.objects.filter(comentario=comentario, user=user).count()
        check2 = DownVote.objects.filter(comentario=comentario, user=user).count()
        bool2 = True
        print(check)
        print(check2)
        if check > 0:
            UpVote.objects.filter(
                comentario=comentario, 
                user=user
                ).delete()
            return JsonResponse({'bool': False})
        elif check == 0:
                        UpVote.objects.create(
                comentario=comentario,
                user=user)
                        if (check2>0):
                            DownVote.objects.filter(comentario=comentario, 
                            user=user
                            ).delete()
                            bool2 = False
                        return JsonResponse({'bool':True})
        else:
            if (check2>0):
                DownVote.objects.filter(comentario=comentario, 
                user=user
                ).delete()
                bool2 = False
            return JsonResponse({'bool2':bool2})
        

# Save Downvote


def save_downvote(request):
    if request.method == 'POST':
        comentarioid = request.POST['comentarioid']
        comentario = Comment.objects.get(pk=comentarioid)
        user = request.user
        check = DownVote.objects.filter(
                comentario=comentario, user=user).count()
        check2 = UpVote.objects.filter(
                comentario=comentario, user=user).count()
        bool2 = True
        if check > 0:
            DownVote.objects.filter(
                comentario=comentario, 
                user=user
                ).delete()
            bool2 = True
            return JsonResponse({'bool':False, 'bool2':bool2})
        elif check == 0:
            print('igual a 0 = '+str(check))
            DownVote.objects.create(
                comentario=comentario,
                user=user
                )
            return JsonResponse({'bool':True})
  
        else:
            print(check2)
            if (check2>0):
                UpVote.objects.filter(
                    comentario=comentario, 
                    user=user
                    ).delete()
                bool2 = False
                return JsonResponse({'bool2':bool2})
            
           