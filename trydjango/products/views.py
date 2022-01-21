#from typing import ContextManager
from django.http import request 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import Http404
#from .forms import ProductForm , RawProductForm

"""
#entering data into a database using forms(raw_html)
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
    my_form = RawProductForm()
    return render(request, 'product/create.html', {'form': my_form})



#instert data using form in a database 
def product_create_view(request):
   form = ProductForm(request.POST or None)

   if form.is_valid():
       form.save()
       form = ProductForm()
   return render(request, 'product/create.html', {'form': form})



#viewing products
def product_detail_view(request):
    info = Product.objects.get(id=1)

    return render(request, 'product/details.html', {'info': info})
"""

#dynamic-lookup
"""def dynamic_lookup_view(request, product_id):
    #info = Product.objects.get(id=product_id)  
    info = get_object_or_404(Product,id=product_id) #getting error 404
    return render(request, 'product/details.html', {'info': info})
   """ 
""" try:
        info = Product.objects.get(id=product_id)  #another way to get error 404
    except Product.DoesNotExist:
        raise Http404
"""
    

def product_delete_view(request, product_id):
    #info = Product.objects.get(id=product_id)  
    info = get_object_or_404(Product,id=product_id) #getting error 404
    if request.method == 'POST':
        info.delete() #confirming delete
        return redirect('/')


    return render(request, 'product/product_delete.html', {'info': info})

