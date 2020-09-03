from django.shortcuts import render, get_object_or_404

from funsite.models import Brand


def index(request):
    """Controller that displays the main page"""
    brand_list = Brand.objects.all()
    context = {'brand_list': brand_list}
    return render(request, "funsite/index.html", context)


def detail_brand(request, pk):
    """The controller displays detailed information about the brand"""
    brand = get_object_or_404(Brand, pk=pk)
    context = {'brand': brand}
    return render(request, 'funsite/detail_brand.html', context)
