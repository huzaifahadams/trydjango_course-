from django.shortcuts import render , get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    

)
from .models import Article
from .forms import ArtcleForm
# Create your views here. 

class ArticleCreateView(CreateView):
    form_class = ArtcleForm
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all() #<blog>/<modelname>_list.html
    
class ArticleDetailView(DetailView):
    template_name = 'articles/article-detail.html'
    queryset = Article.objects.all() 

""" def get_object(self):
        id_ = self.kwargs.get(id)
        return get_object_or_404(Article, id=id_)
"""