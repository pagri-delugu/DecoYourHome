from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from .forms import contactForm, reviewForm
from .models import Product

# BASE TEMPLATE, DO NOT TOUCH!!!
def base(request):
    return render(request, 'pages/base.html')

# DYNAMIC TEMPLATES BELOW
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    content = {'product': product}
    return render(request, 'pages/product_detail.html', content)