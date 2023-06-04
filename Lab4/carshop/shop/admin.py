from django.contrib import admin
from .models import Order, Product, ProductInstance, Manufacturer, Supplier


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print("SAFKGKWEKGNEKG::AGAGKLAE:MGA:K")
        obj.save()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'unit_price', 'date_of_import')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_products', 'address', 'phone')


class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code')
    inlines = [ProductInstanceInline]


@admin.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'product', 'manufacturer', 'status', 'price')
    list_filter = ('status', 'price')
