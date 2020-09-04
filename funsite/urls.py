from django.urls import path

from funsite.views import index, detail_brand, detail_news

urlpatterns = [
    path('', index, name='index'),
    path('brand/<int:pk>/', detail_brand, name='detail_brand'),
    path('news/<int:pk>/', detail_news, name='detail_news')
]