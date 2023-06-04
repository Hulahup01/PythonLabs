from django.contrib import admin
from .models import Order, Product, ProductInstance, Manufacturer, Supplier

#admin.site.register(Stuff)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'manufacturer', 'quantity', 'unit_price', 'date_of_import', 'supplier')
    fields = [('product', 'manufacturer'), ('quantity', 'unit_price'), 'supplier', 'date_of_import']

    def save_model(self, request, obj, form, change):
        product = obj.product
        manufacturer = obj.manufacturer
        product_instance = ProductInstance.objects.filter(product=product, manufacturer=manufacturer)
        if product_instance.exists() and len(product_instance) == 1:
            product_instance = product_instance[0]
            product_instance.quantity += obj.quantity
            if product_instance.quantity != 0 and product_instance.status == 'n':
                product_instance.status = 'a'
            product_instance.save()
        else:
            raise Exception
        obj.save()


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
