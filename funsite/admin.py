from django.contrib import admin

# Register your models here.
from funsite.models import Brand, News, Carousel, CompanyInfo, Department, Address, Country, City, Street


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


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    """Displaying the info about department in the admin panel"""
    inlines = [AddressInline, ]
    list_display = ('name_department',)


class AddressAdmin(admin.ModelAdmin):
    """Displaying the info about street in the admin panel"""
    list_display = ('title', 'department', 'country', 'city', 'street', 'number_house',
                    'number_flat', 'number_office')


admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Street)
