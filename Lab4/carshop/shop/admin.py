from django.contrib import admin
from .models import Order, Product, ProductInstance, Manufacturer, Supplier

#admin.site.register(Order)
#admin.site.register(Product)
#admin.site.register(ProductInstance)
#admin.site.register(Manufacturer)
#admin.site.register(Supplier)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'unit_price', 'date_of_import')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_products', 'address', 'phone')


class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code', 'manufacturer')
    inlines = [ProductInstanceInline]


@admin.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'status', 'price', 'date_of_purchase')
    list_filter = ('status', 'price')


admin.site.register(Supplier, SupplierAdmin)

