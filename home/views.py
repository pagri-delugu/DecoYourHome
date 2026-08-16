from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from .forms import contactForm, reviewForm
from .models import Product

# BASE TEMPLATE, DO NOT TOUCH!!!
def base(request):
    return render(request, 'pages/base.html')

# DYNAMIC TEMPLATES BELOW
def home(request):
    products = Product.objects.all()
    context = {
        'products_list': products
    }
    return render(request, 'pages/home.html', context)

def search(request):
    query = request.GET.get('q', '').strip()
    
    # Lọc sản phẩm theo tên (không phân biệt hoa/thường)
    results = Product.objects.filter(name__icontains=query) if query else []

    context = {
        'keyword': query,
        'products': results,
    }
    return render(request, 'pages/search.html', context)