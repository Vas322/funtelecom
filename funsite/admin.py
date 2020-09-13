from django.contrib import admin

# Register your models here.
from funsite.models import Brand, News, Carousel, CompanyInfo


class BrandAdmin(admin.ModelAdmin):
    """Displaying a brand in the admin panel"""
    fieldsets = [
        ('Введите название бренда', {'fields': ['name']}),
        ('Введите ссылку на сайт', {'fields': ['link_site']}),
        ('Введите описание бренда', {'fields': ['text'[:20]]}),
        ('Выберите логотип бренда', {'fields': ['image_brand']}),
    ]
    list_display = ('name', 'link_site')


class NewsAdmin(admin.ModelAdmin):
    """Displaying a News in the admin panel"""
    fieldsets = [
        ('Введите оглавление новости', {'fields': ['title']}),
        ('Введите описание новости', {'fields': ['text'[:20]]}),
        ('Выберите изображение новости', {'fields': ['image_news']}),
    ]
    list_display = ('title', 'created_date')


class CarouselAdmin(admin.ModelAdmin):
    """Displaying a Carousel in the admin panel"""
    fieldsets = [
        ('Введите оглавление новости для карусели', {'fields': ['title']}),
        ('Выберите изображение карусели', {'fields': ['image_carousel']}),
        ('Ведите ссылку на новость или товар', {'fields': ['link']}),
        ('Установите приоритет', {'fields': ['index']}),

    ]
    list_display = ('title', 'created_date', 'link', 'index')


class CompanyInfoAdmin(admin.ModelAdmin):
    """Displaying the info about company in the admin panel"""
    list_display = ('title', 'description')


admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Carousel, CarouselAdmin)
