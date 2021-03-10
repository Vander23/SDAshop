from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Brand, CarModel, Product

def home(request):
    return render(request, 'home.html')

def produkt1(request):
    return render(request, 'produkt1.html')

def produkt2(request):
    return render(request, 'produkt2.html')

def produkt3(request):
    return render(request, 'produkt3.html')

def informacje_o_zamowieniu(request):
    return render(request, 'infozam.html')

def reklamacje(request):
    return render(request, 'reklamacje.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def co_sprzedajemy(request):
    return render(request, 'cosprzedajemy.html')

def zwroty(request):
    return render(request, 'zwroty.html')


@login_required
def panel(request):
    return render(request, 'home.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id, in_stock=True)
    return render(request, 'single_product.html', {'product': product})
