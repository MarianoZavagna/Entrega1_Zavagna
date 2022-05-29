from django.urls import path

from app_coder import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('products', views.products, name='Products'),
    path('technologies', views.technologies, name='Technologies'),
    path('users', views.users, name='Users'),
    path('orders', views.orders, name='Orders'),
    path('formHTML', views.form_hmtl),
    path('technology-django-forms', views.technology_forms_django, name='TechnologyDjangoForms'),
    path('product-django-forms', views.product_forms_django, name='ProductDjangoForms'),
    path('order-django-forms', views.order_forms_django, name='OrderDjangoForms'),
    path('user-django-forms', views.user_forms_django, name='UserDjangoForms'),
    path('search', views.search, name='Search'),
]
