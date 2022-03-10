from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "description", "price", "sale_price"]
    search_fields = ["title", "description"]
    list_filter = ["price", "sale_price"]
    list_editable = ["sale_price"]
    class Meta:
        model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name"]
    search_fields = ["name"]
    list_filter = ["name"]
    list_editable = ["name"]
    class Meta:
        model = Category


admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)