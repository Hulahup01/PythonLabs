from django.contrib import admin
from .models import Order, Product, ProductInstance, Manufacturer, Supplier

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductInstance)
admin.site.register(Manufacturer)
admin.site.register(Supplier)
