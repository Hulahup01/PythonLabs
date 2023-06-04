from django.shortcuts import render
from .models import Order, Product, ProductInstance, Manufacturer, Supplier
from django.views import generic


def index(request):
    num_products = Product.objects.all().count()
    num_instances = ProductInstance.objects.all().count()
    num_instances_available = ProductInstance.objects.filter(status__exact='a').count()
    num_manuf = Manufacturer.objects.count()
    return render(
        request,
        'index.html',
        context={'num_products': num_products, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_manuf': num_manuf},
    )


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 1


class ProductDetailView(generic.DetailView):
    model = Product


