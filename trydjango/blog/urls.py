from django.urls import path
#from django.urls.resolvers import URLPattern
#from django.views.generic import View
from .views import (
    ArticleCreateView,
    ArticleDetailView
    
    )




app_name = 'articles'
urlpatterns = [
    #path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/',ArticleDetailView.as_view(), name='article-detail')
    #path('<str:id>/update', view_name, name='article-update').
    #path('<str:id>/delete', view_name, name='article-delete').
]

