from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from funsite.models import Brand, News


def index(request):
    """Controller that displays the main page"""
    brand_list = Brand.objects.all()
    news_list = News.objects.order_by('-created_date')[:3]
    context = {'brand_list': brand_list, 'news_list': news_list}
    return render(request, "funsite/index.html", context)


def detail_brand(request, pk):
    """The controller displays detailed information about the brand"""
    brand = get_object_or_404(Brand, pk=pk)
    context = {'brand': brand}
    return render(request, 'funsite/detail_brand.html', context)


def detail_news(request, pk):
    """The controller displays detailed information about the news"""
    news = get_object_or_404(News, pk=pk)
    context = {'news': news}
    return render(request, 'funsite/detail_news.html', context)
