from django.urls import path

from funsite.views import index, detail_brand, detail_news, all_news, all_brands, company_info

urlpatterns = [
    path('', index, name='index'),
    path('brand/<int:pk>/', detail_brand, name='detail_brand'),
    path('news/<int:pk>/', detail_news, name='detail_news'),
    path('all_news/', all_news, name='all_news'),
    path('', all_brands, name='all_brands'),
    path('company_info', company_info, name='company_info'),
]