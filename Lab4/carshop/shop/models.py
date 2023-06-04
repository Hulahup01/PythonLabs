from django.db import models
from django.urls import reverse
#from django.contrib.auth.models import AbstractUser
import uuid


# class Stuff(AbstractUser):
#     bio = models.TextField(
#         'Biography',
#         blank=True,
#     )


class Product(models.Model):
    name = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])


class ProductInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this product")
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)

    AVAILABLE_STATUS = (
        ('a', 'Available'),
        ('n', 'Not in stock'),
    )

    status = models.CharField(max_length=1, choices=AVAILABLE_STATUS, blank=True,
                              default='a', help_text='Product availability')

    class Meta:
        ordering = ['price', 'product']

    def __str__(self):
        return f'{self.id} ({self.product.name})'

    def get_absolute_url(self):
        return reverse('product_instance-detail', args=[str(self.id)])


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)

    def get_absolute_url(self):
        return reverse('Supplier-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

    def display_products(self):
        return ', '.join(product.name for product in self.products.all()[:3])
    display_products.short_description = 'Products'


class Order(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    date_of_import = models.DateField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['quantity']

    def __str__(self):
        return f"'{self.product}' ord: {self.date_of_import} - {self.quantity} units"

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])
