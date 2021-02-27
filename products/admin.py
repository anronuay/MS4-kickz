from django.contrib import admin
from .models import Product, Brand


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "brand",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
