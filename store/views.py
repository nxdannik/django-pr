from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html')

def contacts(request):
    return render(request, 'store/contacts.html')

def delivery(request):
    return render(request, 'store/delivery.html')

def payment(request):
    return render(request, 'store/payment.html')
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()[:6]  # Показати перші 6 товарів
    return render(request, 'index.html', {'products': products})
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.product_set.all()
    return render(request, 'category_detail.html', {'category': category, 'products': products})