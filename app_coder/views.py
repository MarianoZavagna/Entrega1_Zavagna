from django.shortcuts import render
from django.db.models import Q

from app_coder.models import Technology, User, Product, Order
from app_coder.forms import TechnologyForm, ProductForm, OrderForm, UserForm


def index(request):
    return render(request, "app_coder/home.html")


def products(request):
    products = Product.objects.all()

    context_dict = {
        'products': products
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/products.html"
    )


def technologies(request):
    technologies = Technology.objects.all()

    context_dict = {
        'technologies': technologies
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/technologies.html"
    )


def users(request):
    users = User.objects.all()

    context_dict = {
        'users': users
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/users.html"
    )


def orders(request):
    orders = Order.objects.all()

    context_dict = {
        'orders': orders
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/orders.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        technology = Technology(name=request.POST['name'], cmodel=request.POST['model'])
        technology.save()

        technologies = Technology.objects.all()
        context_dict = {
            'technology': technologies
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/technologies.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def technology_forms_django(request):
    if request.method == 'POST':
        technology_form = TechnologyForm(request.POST)
        if technology_form.is_valid():
            data = technology_form.cleaned_data
            technology = Technology(name=data['name'], model=data['model'])
            technology.save()

            technologies = Technology.objects.all()
            context_dict = {
                'technologies': technologies
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/technologies.html"
            )

    technology_form = TechnologyForm(request.POST)
    context_dict = {
        'technology_form': technology_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/technology_django_forms.html'
    )


def product_forms_django(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            data = product_form.cleaned_data
            product = Product(
                name=data['name'],
                code=data['code'],
            )
            product.save()

            products = Product.objects.all()
            context_dict = {
                'products': products
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/products.html"
            )

    product_form = ProductForm(request.POST)
    context_dict = {
        'product_form': product_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/product_django_forms.html'
    )


def order_forms_django(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            data = order_form.cleaned_data
            order = Order(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            order.save()

            orders = Order.objects.all()
            context_dict = {
                'orders': orders
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/orders.html"
            )

    order_form = OrderForm(request.POST)
    context_dict = {
        'order_form': order_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/order_django_forms.html'
    )


def user_forms_django(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user = User(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                phone=data['phone'],
                profession=data['profession'],
            )
            user.save()

            users = User.objects.all()
            context_dict = {
                'users': users
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/users.html"
            )

    user_form = UserForm(request.POST)
    context_dict = {
        'user_form': user_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/user_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        products = Product.objects.filter(name__contains=search_param)
        context_dict = {
            'products': products
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        products = Product.objects.filter(code__contains=search_param)
        context_dict = {
            'products': products
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        products = Product.objects.filter(query)
        context_dict = {
            'products': products
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )
