"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pages.views import about, contact, home, login, logout, register
from products.views import  product_delete_view #product_detail_view # product_create_view #dynamic_lookup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', include('pages.urls')),
    path('blog/', include('blog.urls')),

    path('', home),
    path('contact',contact),
    path('about', about),
    path('login', login ),
    path('logout', logout),
    path('register', register),
    #path('product', product_detail_view),
   # path('create', product_create_view),
    #path('product/<str:product_id>', dynamic_lookup_view, name='product'),
    path('product/<str:product_id>', product_delete_view, name='product_delete')


]



