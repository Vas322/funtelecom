from django.contrib import admin

# Register your models here.
from funsite.models import Brand


class BrandAdmin(admin.ModelAdmin):
    """Displaying a brand in the admin panel"""
    fieldsets = [
        ('Введите название бренда', {'fields': ['name']}),
        ('Введите ссылку на сайт', {'fields': ['link_site']}),
        ('Введите описание бренда', {'fields': ['text'[:20]]}),
        ('Выберите логотип бренда', {'fields': ['image_brand']}),
    ]
    list_display = ('name', 'link_site')


admin.site.register(Brand, BrandAdmin)
