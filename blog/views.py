from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article

def home(request):
  articles_list = Article.objects.filter(status="p").order_by('-published')

  context = {'articles_list': articles_list}
  return render(request, 'blog/index.html', context)

def detail(request, slug):

  article_detail = get_object_or_404(Article, slug=slug, status="p")
  context= {'article_detail': article_detail}

  return render(request, 'blog/post.html', context)