from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Brand, CarModel, Product

def home(request):
    return render(request, 'home.html')


def searching(request):
    return render(request, 'searching.html')

def add(request):
    return render(request, 'add.html')

def contact(request):
    return render(request, 'contact.html')


@login_required
def panel(request):
    return render(request, 'home.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id, in_stock=True)
    return render(request, 'single_product.html', {'product': product})
