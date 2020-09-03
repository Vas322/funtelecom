from django.urls import path

from funsite.views import index, detail_brand

urlpatterns = [
    path('', index, name='index'),
    path('brand/<int:pk>/', detail_brand, name='detail_brand')
]