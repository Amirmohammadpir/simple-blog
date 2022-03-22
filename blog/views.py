from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Category

def home(request):

  context = {'articles_list': Article.objects.filter(status="p"),}

  return render(request, 'blog/index.html', context)


def detail(request, slug):

  context= {'article_detail': get_object_or_404(Article, slug=slug, status="p")}

  return render(request, 'blog/post.html', context)


def category(request, slug):
  
  context= {'category': get_object_or_404(Category, slug=slug, status=True)}

  return render(request, 'blog/category.html', context)
