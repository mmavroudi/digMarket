from django.shortcuts import render, get_object_or_404

from products.models import Product


def home_view(request, template_path='home.html'):
    """
    Markeplace home
    """
    products = Product.objects.all()

    context = dict(
        products=products
    )
    return render(request, template_path, context)
