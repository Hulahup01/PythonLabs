from django.shortcuts import render
from .models import Order, Product, ProductInstance, Manufacturer, Supplier
from django.views import generic


def index(request):
    num_products = Product.objects.all().count()
    num_instances = ProductInstance.objects.all().count()
    num_instances_available = ProductInstance.objects.filter(status__exact='a').count()
    num_manuf = Manufacturer.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_products': num_products, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_manuf': num_manuf, 'num_visits': num_visits},
    )


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10


class ProductDetailView(generic.DetailView):
    model = Product


