from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.views.generic import DetailView

def news(request):
    search_query = request.GET.get('search', '')
    if search_query:
        news = Article.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))
    else:
       news = Article.objects.all()
    return render(request, 'news/news.html', {'news': news})




class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'



