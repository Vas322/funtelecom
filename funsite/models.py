from django.db import models
from datetime import datetime
from os.path import splitext
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


def get_timestamp_path(instance, filename):
    """The function creates picture names based on the current date"""
    return "%s%s" % (datetime.now().timestamp(), splitext(filename)[1])


class Brand(models.Model):
    """The model describes the brand"""
    name = models.CharField(max_length=200, verbose_name='Название бренда*')
    text = models.TextField(verbose_name='Описание бренда*')
    link_site = models.CharField(max_length=200, verbose_name='Ссылка на сайт')
    image_brand = models.ImageField(blank=True, upload_to=get_timestamp_path,
                                    verbose_name='Загрузить изображение*')

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        img = Image.open(self.image_brand.path)

        if img.height > 200 or img.width > 200:
            output_size_brand = (200, 200)
            img.thumbnail(output_size_brand)
            img.save(self.image_brand.path)

    class Meta:
        """Attribute allows you to use the plural form of 'Brands'"""
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class News(models.Model):
    """The model news"""
    title = models.CharField(max_length=200, verbose_name='Название новости')
    text = models.TextField(verbose_name='Текст новости')
    image_news = models.ImageField(blank=True, upload_to=get_timestamp_path,
                                   verbose_name='Загрузить изображение* Изображение должно'
                                                'быть квадратным для корректного отображения')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True,
                                        verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.image_news.path)

        if img.height > 400 or img.width > 400:
            output_size_news = (400, 400)
            img.thumbnail(output_size_news)
            img.save(self.image_news.path)

    class Meta:
        """Attribute allows you to use the plural form of 'News'"""
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Carousel(models.Model):
    """The model carousel"""
    title = models.CharField(max_length=200, verbose_name='Название новости в карусели')
    image_carousel = models.ImageField(blank=True, upload_to=get_timestamp_path,
                                       verbose_name='Загрузить изображение*. Рекомендуемые '
                                                    'размеры: 1000х400 пикселей!')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True,
                                        verbose_name='Дата публикации')
    link = models.CharField(max_length=255, verbose_name='Ссылка на новость, товар или сайт.')
    index = models.IntegerField(verbose_name='Индекс приоритета отображения',
                                help_text='Введите число от 0 до 10. 0 имеет самый высокий приоритет.')

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.image_carousel.path)

        if img.width > 1000 or img.height > 400:
            output_size_carousel = (1000, 400)
            img.thumbnail(output_size_carousel)
            img.save(self.image_carousel.path)

    class Meta:
        """Attribute allows you to use the plural form of 'carousels'"""
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусель'


class CompanyInfo(models.Model):
    """Model with company information"""
    title = models.CharField(max_length=100, verbose_name='Название Компании')
    description = models.TextField(verbose_name='Описание компании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Инфо о компании'
        verbose_name_plural = 'Инфо о компании'


class Department(models.Model):
    """The model describes the department of the company."""
    name_department = models.CharField(max_length=50, verbose_name='Название подразделения',
                                       help_text='Например, Офис')
    working_hours = models.CharField(max_length=30, verbose_name='Часы работы',
                                     help_text='Пример: С 9-00 до 18-00')
    email_department = models.ForeignKey('Email', on_delete=models.CASCADE,
                                         verbose_name='Эл.почта подразделения')
    phone_department = models.ForeignKey('Phone', on_delete=models.CASCADE,
                                         verbose_name='Телефон подразделения')
    department_address = models.ForeignKey('Address', on_delete=models.CASCADE,
                                           verbose_name='Адрес подразделения')
    published_on_page = models.BooleanField(default=False, verbose_name='Опубликовано',
                                            help_text='Публиковать информацию о подразделении на странице?')

    def __str__(self):
        return self.name_department

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Address(models.Model):
    """The model describes the address"""
    title = models.CharField(max_length=50, blank=True, verbose_name='Описание адреса',
                             help_text='Например, Адрес склада')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Населенный пункт')
    street = models.ForeignKey('Street', on_delete=models.CASCADE, null=True, verbose_name='Улица')
    number_house = models.PositiveSmallIntegerField(verbose_name='Номер дома', null=True, blank=True, validators=[
        MaxValueValidator(1000), MinValueValidator(1)])
    number_flat = models.PositiveSmallIntegerField(verbose_name='Номер помещения', blank=True, null=True, validators=[
        MaxValueValidator(1000), MinValueValidator(1)])
    number_office = models.PositiveSmallIntegerField(verbose_name='Номер офиса', blank=True, null=True, validators=[
        MaxValueValidator(1000), MinValueValidator(1)])
    access_map_link = models.CharField(max_length=255, verbose_name='Ссылка на схему проезда', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адрес'


class Country(models.Model):
    """The model describes the country"""
    name_country = models.CharField(max_length=56, verbose_name='Название страны',
                                    validators=[RegexValidator(regex=r'^[a-zA-Zа-яА-Я]+$')])

    def __str__(self):
        return self.name_country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class City(models.Model):
    """The model describes the city"""
    name_city = models.CharField(max_length=56, verbose_name='Название города',
                                 validators=[RegexValidator(regex=r'^[a-zA-Zа-яА-Я0-9]+$')])

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    """The model describes the street"""
    name_street = models.CharField(max_length=56, verbose_name='Название улицы',
                                   validators=[RegexValidator(regex=r'^[a-zA-Zа-яА-Я0-9]+$')],
                                   help_text='Если в списке нет улицы, то внесите ее нажав на "+"')

    def __str__(self):
        return self.name_street

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улица'


class Email(models.Model):
    """The model stores contact information"""
    email = models.EmailField(max_length=150, verbose_name='email адрес')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Электронная почта'
        verbose_name_plural = 'Электронная почта'


class Phone(models.Model):
    """The model stores phone numbers"""
    phone_number = PhoneNumberField(verbose_name='Введите номер телефона')
    extension_number = models.PositiveIntegerField(verbose_name='Добавочный номер', blank=True, null=True,
                                                   validators=[MaxValueValidator(100000), MinValueValidator(1)])

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = 'Телефонный номер'
        verbose_name_plural = 'Телефоннные номера'


class Partner(models.Model):
    """The Model stores partner information"""
    name_partner_company = models.CharField(max_length=200, verbose_name='Название вашей компании')
    target_registration = models.CharField(max_length=100, verbose_name='Цель заявки', null=True,
                                           help_text='Например, покупка товаров оптом.')
    position_partner_on_market = models.CharField(max_length=100, verbose_name='Позиция на рынке', null=True,
                                                  help_text='Например, "Интегратор"')

    def __str__(self):
        return self.name_partner_company

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Employee(models.Model):
    """The model stores information about partner's employee"""
    last_name = models.CharField(max_length=100, verbose_name='Фамилия',
                                 validators=[RegexValidator(regex=r'^[a-zA-Zа-яА-Я]+$')])
    first_name = models.CharField(max_length=100, verbose_name='Имя',
                                  validators=[RegexValidator(regex=r'^[a-zA-Zа-яА-Я]+$')])
    employee_position = models.ForeignKey('EmployeePosition', on_delete=models.CASCADE,
                                          verbose_name='Должность сотрудника')
    email_employee = models.ForeignKey('Email', on_delete=models.CASCADE, verbose_name='Эл.почта сотрудника')
    phone_employee = models.ForeignKey('Phone', on_delete=models.CASCADE, verbose_name='Номер телефона сотрудника')
    address_employee = models.ForeignKey('Address', on_delete=models.CASCADE, null=True,
                                         verbose_name='Адрес сотрудника')
    name_partner = models.ForeignKey('Partner', on_delete=models.CASCADE, null=True,
                                     verbose_name='Работает в компании')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class EmployeePosition(models.Model):
    """The model stores information about employee position"""
    title = models.CharField(max_length=100, verbose_name='Должность сотрудника')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должность сотрудника'


class MailToSupport(models.Model):
    """The model sending email to support"""
    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    name = models.CharField(max_length=30, null=True, verbose_name='Ваше имя')
    equipment_name = models.CharField(max_length=100, null=True, verbose_name='Наименование оборудования')
    serial_number = models.CharField(max_length=50, null=True, verbose_name='Серийный номер оборудования')
    sender = models.EmailField(max_length=150, verbose_name='Ваш email для ответа')
    message = models.TextField(verbose_name='Детально опишите вашу проблему')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Письмо в техподдержку'
        verbose_name_plural = 'Письма в техподдержку'
