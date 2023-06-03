from django.db import models
from django.urls import reverse
import uuid


class Product(models.Model):
    name = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=10)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])


class ProductInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this product")
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    date_of_purchase = models.DateField(null=True, blank=True)

    AVAILABLE_STATUS = (
        ('a', 'Available'),
        ('n', 'Not in stock'),
    )

    status = models.CharField(max_length=1, choices=AVAILABLE_STATUS, blank=True,
                              default='a', help_text='Product availability')

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f'{self.id} ({self.product.name})'


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


class Order(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_import = models.DateField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['quantity']

    def __str__(self):
        return f"Ordered on {self.date_of_import} - {self.quantity} units"

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])