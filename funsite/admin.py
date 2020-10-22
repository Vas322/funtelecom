from django.contrib import admin

# Register your models here.
from funsite.models import Brand, News, Carousel, CompanyInfo, Department, Address, Country, \
    City, Street, Phone, Partner, Email, Employee, EmployeePosition, MailToSupport


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


class DepartmentAdmin(admin.ModelAdmin):
    """Displaying the info about department in the admin panel"""
    list_display = ('name_department', 'phone_department', 'email_department', 'working_hours', 'published_on_page')
    list_display_links = ('name_department', 'phone_department', 'email_department')


class AddressAdmin(admin.ModelAdmin):
    """Displaying the info about street in the admin panel"""
    list_display = ('title', 'country', 'city', 'street', 'number_house',
                    'number_flat', 'number_office')
    search_fields = ['country__name_country', 'city__name_city', 'street__name_street']


class CountryAdmin(admin.ModelAdmin):
    """Displaying the info about country in the admin panel"""

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


class CityAdmin(admin.ModelAdmin):
    """Displaying the info about city in the admin panel"""

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


class StreetAdmin(admin.ModelAdmin):
    """Displaying the info about street in the admin panel"""

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


class EmailAdmin(admin.ModelAdmin):
    """
    Hiding an email in the admin panel.But email is available when add related models
    """

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


class PartnerAdmin(admin.ModelAdmin):
    """Displaying the info about partner in the admin panel"""
    list_display = ('name_partner_company', 'position_partner_on_market', 'target_registration',)
    search_fields = ['name_partner_company', 'position_partner_on_market', 'target_registration']
    list_display_links = ('name_partner_company',)


class EmployeeAdmin(admin.ModelAdmin):
    """Displaying the info about partner's employee in the admin panel"""
    list_display = ('last_name', 'first_name', 'employee_position', 'email_employee', 'phone_employee', 'name_partner',
                    'address_employee')
    search_fields = ['last_name', 'employee_position', 'email_employee', 'name_partner']
    list_display_links = ('address_employee', 'last_name')


class EmployeePositionAdmin(admin.ModelAdmin):
    """Hiding information about an employee's position in the admin panel.
        But EmployeePosition is available when add related models
        """

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


class MailToSupportAdmin(admin.ModelAdmin):
    """Displaying a messages to support in the admin panel"""
    list_display = ('subject', 'name', 'equipment_name', 'serial_number', 'sender', 'message')


admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(Phone, CountryAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeePosition, EmployeePositionAdmin)
admin.site.register(MailToSupport, MailToSupportAdmin)
