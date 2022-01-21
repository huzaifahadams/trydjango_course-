from django import forms
from django.db import models
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Textarea 
from .models import Product

class ProductForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'cool title '}))
    discription = forms.CharField(widget=forms.Textarea(
        attrs={
             'class': 'new-class-x',
             'rows': 20,
             'cols':100,
             'placeholder':'your great discription '
    }))
    price = forms.DecimalField(initial=199.99)
    summury = forms.CharField()
    Email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'enter a business email '}))

    class  Meta:
       model = Product
       fields = [
           'title',
           'discription',
           'price',
           'summury'
       ]
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith(['gmail', 'yahoo', 'protonmail']):
            raise forms.ValidationError('Enter a valid email for yoour business ')
        return email



class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your title '}))
    discription = forms.CharField(widget=forms.Textarea(
        attrs={
             'class': 'new-class-x',
             'rows': 20,
             'cols':100,
             'placeholder':'your great discription '
    }))
    price = forms.DecimalField(initial=199.99)
    summury = forms.CharField()

    
