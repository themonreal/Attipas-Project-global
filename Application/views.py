from django.shortcuts import render
from Application.models import Size, Product

def index(request):
    size = Size.objects.all()
    product = Product.objects.all()
    context = {
    'size': size,
    'product': product
    }

    return render(request,'Application/index1.html', context)

def product_view(request,product_slug):
    product=Product.objects.get(slug=product_slug)
    context = {
    'product' : product
    }
    return render(request, 'product.html', context)

def size_view(request,product_slug):
    size=Product.objects.get(slug=size_slug)
    context = {
    'size' : product
    }
    return render(request, 'size.html', context)
