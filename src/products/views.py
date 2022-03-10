from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product
from .models import Category

def detail_slug_view(request, slug=None):
    product = Product.objects.get(slug=slug)
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()
    # print slug
    # product = 1
    template = "detail_view.html"
    context = {
        "object": product
        }
    return render(request, template, context)

def category_slug_view(request, slug=None):
    category = Category.objects.get(slug=slug)
    try:
        category = get_object_or_404(Category, slug=slug)
    except Category.MultipleObjectsReturned:
        category = Category.objects.filter(slug=slug).order_by("-name").first()

    template = "category_view.html"
    context = {
        "object": category
        }
    return render(request, template, context)

def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template, context)


def list_view(request):
    #list of items
    print(request)
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset": queryset
    }
    return render(request, template, context)

def category_view(request, object_id=None):
    category = get_object_or_404(Category, id=object_id)
    template = "category_view.html"
    context = {
        "object": category
    }
    return render(request, template, context)


