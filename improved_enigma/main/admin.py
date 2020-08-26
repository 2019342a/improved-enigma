from django.contrib import admin

from .models import Customer
from .models import Order
from .models import Product
from .models import Stock


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "email")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    raw_id_fields = ("customer",)
    list_select_related = ("customer",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    raw_id_fields = ("product",)
    list_select_related = ("product",)
