from django.contrib import admin
from apps.catalog.models import Product, Filial, FilialPrice, Characteristic


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("id", "name")
    list_display = ("id", "name")


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    search_fields = ("id", "name", "region")
    list_display = ("id", "name", "region")


@admin.register(FilialPrice)
class FilialPriceAdmin(admin.ModelAdmin):
    search_fields = ("id", "price")
    list_display = ("id", "product_id", "filial_id", "price")
    filter = ("filial_id",)


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    search_fields = ("id", "name")
    list_display = ("id", "name", "self")
