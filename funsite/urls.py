from django.urls import path

from funsite.views import index

urlpatterns = [
    path('', index, name='index'),
]