
from django.urls import path

from .import views
#from ..products import product_detail_view
#from ..products import views
#from ..products.views import product_detail_view
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    #path('product', views.product_detail_view, name='product_detail_view'),

]
