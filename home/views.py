from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from .models import Product, Banner, Post

# BASE TEMPLATE, DO NOT TOUCH!!!
def base(request):
    return render(request, 'pages/base.html')

# DYNAMIC TEMPLATES BELOW
def home(request):
    banner   = Banner.objects.filter(is_active=True)
    products = Product.objects.filter(in_stock=True).order_by('-sold_quantity')[:4] # Only takes 4 in-stock products with highest sales

    context  = {
        'banner': banner,
        'products': products
    }

    return render(request, 'pages/home.html', context)

def search(request):
    query   = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) if query else []

    context = {
        'keyword': query, 
        'products': results
    }

    return render(request, 'pages/search.html', context)

def product_list(request):
    products = Product.objects.all()
    
    return render(request, 'pages/product_list.html', {'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, pk=id) # Variable name for this view's context is "product" without "s" ("products" is incorrect)

    return render(request, 'pages/product_detail.html', {'product': product})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse("Cảm ơn bạn đã phản hồi với chúng tôi")

    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

def news(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'pages/news.html', {'posts': posts})

def news_article(request):
    post = get_object_or_404(Post, pk=id) # Variable name for this view's context is "post" without "s" ("posts" is incorrect)

    return render(request, 'pages/article.html', {'post': post})