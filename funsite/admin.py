from django import forms
from django.contrib import admin

# Register your models here.
from django.urls import reverse

from funsite.forms import NewsAdminForm
from funsite.models import Brand, News, Carousel, CompanyInfo, Department, Country, \
    City, Street, Phone, Partner, Email, Employee, EmployeePosition, MailToSupport, NumberHouse, NumberOffice, \
    AccessMapLink
from django.utils.html import format_html, mark_safe


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Displaying a brand in the admin panel"""

    list_display = ('name', 'link_site', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image_brand.url} width="80"')

    get_image.short_description = "Изображение бренда"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Displaying a News in the admin panel"""
    form = NewsAdminForm
    fieldsets = [
        ('Введите оглавление новости', {'fields': ['title']}),
        ('Введите описание новости', {'fields': ['text'[:20]]}),
        ('Выберите изображение новости', {'fields': (('image_news', 'get_image'),)}),
        ('Дата создания новости', {'fields': ['created_date']}),
    ]
    readonly_fields = ('get_image', 'created_date',)
    list_display = ('title', 'created_date', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image_news.url} width="120"')

    get_image.short_description = "Изображение"


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """Displaying a Carousel in the admin panel"""
    fieldsets = [
        ('Введите оглавление новости для карусели', {'fields': ['title']}),
        ('Выберите изображение карусели', {'fields': ['image_carousel']}),
        ('Ведите ссылку на новость или товар', {'fields': ['link']}),
        ('Установите приоритет', {'fields': ['index']}),
        ('Дата создания баннера', {'fields': ['created_date']}),
    ]
    list_display = ('title', 'created_date', 'link', 'index')
    readonly_fields = ('created_date',)
    list_editable = ('index',)


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    """Displaying the info about company in the admin panel"""
    fieldsets = [
        ('Введите название компании', {'fields': ['title']}),
        ('Введите описание компании', {'fields': ['description'[:20]]}),
    ]
    list_display = ('title', 'description')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Displaying the info about department in the admin panel"""
    list_display = ('name_department', 'phone_department', 'email_department', 'working_hours', 'published_on_page')
    list_display_links = ('name_department', 'phone_department', 'email_department')
    list_editable = ('published_on_page',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Displaying the info about country in the admin panel"""

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Displaying the info about city in the admin panel"""

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    """Displaying the info about street in the admin panel"""

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    """
    Hiding an email in the admin panel.But email is available when add related models
    """

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 0


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """Displaying the info about partner in the admin panel"""
    model = Partner

    list_display = ('name_partner_company', 'position_partner_on_market', 'target_registration',)
    fields = (('name_partner_company', 'position_partner_on_market', 'target_registration'),)
    search_fields = ['name_partner_company', 'position_partner_on_market', 'target_registration']
    list_display_links = ('name_partner_company',)

    inlines = [
        EmployeeInline,
    ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Displaying the info about partner's employee in the admin panel"""
    model = Employee
    radio_fields = {"employee_position": admin.VERTICAL}
    fields = (('last_name', 'first_name'), 'employee_position', ('country_employee', 'city_employee', 'email_employee',
                                                                 'phone_employee'), 'name_partner')
    list_display = ('last_name', 'first_name', 'employee_position', 'email_employee', 'phone_employee',
                    'country_employee', 'city_employee', 'partner_link', 'get_position_partner_on_market')
    search_fields = ['last_name', 'employee_position', 'email_employee', 'name_employee']
    list_display_links = ('last_name', 'partner_link')
    list_filter = ('city_employee', 'name_partner')
    save_on_top = True

    def get_position_partner_on_market(self, obj):
        employee_obj = obj.name_partner.position_partner_on_market
        return employee_obj

    get_position_partner_on_market.short_description = 'Позиция на рынке'

    def partner_link(self, obj: Employee):
        url = reverse('admin:funsite_partner_change', args=[obj.name_partner.id])
        link = f'<a href="{url}">{obj.name_partner.name_partner_company}</a>'
        return mark_safe(link)

    partner_link.short_description = 'Имя партнера'


@admin.register(NumberHouse)
class NumberHouseAdmin(admin.ModelAdmin):
    """Hiding information about an employee's position in the admin panel.
        But EmployeePosition is available when add related models
        """

    """def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}"""


@admin.register(NumberOffice)
class NumberOfficeAdmin(admin.ModelAdmin):
    """Hiding information about an employee's position in the admin panel.
        But EmployeePosition is available when add related models
        """

    """def get_model_perms(self, request):

        Return empty perms dict thus hiding the model from admin index.

        return {}"""


@admin.register(AccessMapLink)
class AccessMapLinkAdmin(admin.ModelAdmin):
    """Hiding information about an employee's position in the admin panel.
        But EmployeePosition is available when add related models
        """

    """def get_model_perms(self, request):

        Return empty perms dict thus hiding the model from admin index.

        return {}"""


@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    """Hiding information about an employee's position in the admin panel.
        But EmployeePosition is available when add related models
        """

    """def get_model_perms(self, request):

        Return empty perms dict thus hiding the model from admin index.

        return {}"""


@admin.register(MailToSupport)
class MailToSupportAdmin(admin.ModelAdmin):
    """Displaying a messages to support in the admin panel"""
    list_display = ('subject', 'name', 'equipment_name', 'serial_number', 'sender', 'message')


admin.site.site_title = "Админка ФАН Телекома"
admin.site.site_header = "Админка ФАН Телекома"
