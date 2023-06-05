from django.shortcuts import render
from .models import Order, Product, ProductInstance, Manufacturer, Supplier
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .forms import SignupForm


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


class OrdersListView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = Order
    paginate_by = 4


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'login'
    model = Product


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context,)
