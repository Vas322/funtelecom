from django.contrib import admin

# Register your models here.
from funsite.models import Brand, News, Carousel, CompanyInfo, Department, Country, \
    City, Street, Phone, Partner, Email, Employee, EmployeePosition, MailToSupport


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Displaying a brand in the admin panel"""
    fieldsets = [
        ('Введите название бренда', {'fields': ['name']}),
        ('Введите ссылку на сайт', {'fields': ['link_site']}),
        ('Введите описание бренда', {'fields': ['text'[:20]]}),
        ('Выберите логотип бренда', {'fields': ['image_brand']}),
    ]
    list_display = ('name', 'link_site')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Displaying a News in the admin panel"""
    fieldsets = [
        ('Введите оглавление новости', {'fields': ['title']}),
        ('Введите описание новости', {'fields': ['text'[:20]]}),
        ('Выберите изображение новости', {'fields': ['image_news']}),
    ]
    list_display = ('title', 'created_date')


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """Displaying a Carousel in the admin panel"""
    fieldsets = [
        ('Введите оглавление новости для карусели', {'fields': ['title']}),
        ('Выберите изображение карусели', {'fields': ['image_carousel']}),
        ('Ведите ссылку на новость или товар', {'fields': ['link']}),
        ('Установите приоритет', {'fields': ['index']}),

    ]
    list_display = ('title', 'created_date', 'link', 'index')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    """Displaying the info about company in the admin panel"""
    list_display = ('title', 'description')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Displaying the info about department in the admin panel"""
    list_display = ('name_department', 'phone_department', 'email_department', 'working_hours', 'published_on_page')
    list_display_links = ('name_department', 'phone_department', 'email_department')


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
                    'country_employee', 'city_employee', 'name_partner', 'get_position_partner_on_market')
    search_fields = ['last_name', 'employee_position', 'email_employee', 'name_employee']
    list_display_links = ('last_name', 'name_partner')
    
    def get_position_partner_on_market(self, obj):
        employee_obj = obj.name_partner.position_partner_on_market
        return employee_obj

    get_position_partner_on_market.short_description = 'Позиция на рынке'


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
