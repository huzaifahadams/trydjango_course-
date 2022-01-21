from django import forms
from .models import  Article


class ArtcleForm(forms.ModelForm):
    class  Meta:
       model = Article
       fields = [
           'title',
           'discription',
           'active',
           
       ]

