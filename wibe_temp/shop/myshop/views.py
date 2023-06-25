from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    return render(request, 'shop/home.html')


def category(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/category.html',
                  {
                      'categories': categories,
                      'products': products
                  })


def all_products(request):
    products = Product.objects.all()
    return render(request, 'shop/product/my_list.html',
                  {
                      'products': products
                  })


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/my_list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    products = Product.objects.all()
    return render(request, 'shop/product/my_detail.html',
                  {
                      'product': product,
                      'products': products
                  })
