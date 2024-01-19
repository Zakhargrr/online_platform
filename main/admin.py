from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from main.models import Product, NetworkNode


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'model', 'release_date')


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'email', 'country', 'city', 'street', 'house_number', 'get_product', 'link_to_supplier', 'category', 'debt',
        'created_at')
    list_display_links = ('name',)
    list_filter = ('city',)
    actions = ('admin_action',)

    @staticmethod
    @admin.display(description='продукты')
    def get_product(obj):
        return [f"{product.product_name} {product.model}" for product in obj.products.all()]

    @staticmethod
    @admin.display(description='поставщик')
    def link_to_supplier(obj):
        if obj.supplier:
            link = reverse("admin:main_networknode_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{} {}</a>', link, obj.supplier.category, obj.supplier.name)
        else:
            return '-'

    @admin.action
    @admin.display(description='admin action')
    def admin_action(self, request, queryset):
        for node in queryset:
            node.debt = 0
            node.save()
