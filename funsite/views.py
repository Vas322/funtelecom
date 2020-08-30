from django.shortcuts import render

from funsite.models import Brand


def index(request):
    """Controller that displays the main page"""
    brand_list = Brand.objects.all()
    context = {'brand_list': brand_list}
    return render(request, "funsite/index.html", context)
