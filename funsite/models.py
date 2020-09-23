from django.db import models
from datetime import datetime
from os.path import splitext
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator


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
    index = models.IntegerField(verbose_name='Индекс приоритета отображения')

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

    class Meta:
        verbose_name = 'Инфо о компании'
        verbose_name_plural = 'Инфо о компании'


class Department(models.Model):
    """The model describes the department of the company."""
    name_department = models.CharField(max_length=50, verbose_name='Название подразделения',
                                       help_text='Например, Офис')
    working_hours = models.CharField(max_length=30, verbose_name='Часы работы',
                                     help_text='Пример: С 9-00 до 18-00')

    def __str__(self):
        return self.name_department

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Address(models.Model):
    """The model describes the address"""
    title = models.CharField(max_length=50, blank=True, verbose_name='Описание адреса',
                             help_text='Например, Адрес склада')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Название подразделения')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    street = models.ForeignKey('Street', on_delete=models.CASCADE, verbose_name='Улица')
    number_house = models.PositiveSmallIntegerField(verbose_name='Номер дома', validators=[
        MaxValueValidator(1000), MinValueValidator(1)])
    number_flat = models.PositiveSmallIntegerField(verbose_name='Номер помещения', blank=True, validators=[
        MaxValueValidator(1000), MinValueValidator(1)])
    number_office = models.PositiveSmallIntegerField(verbose_name='Номер офиса', blank=True, validators=[
        MaxValueValidator(1000), MinValueValidator(1)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Country(models.Model):
    """The model describes the country"""
    name_country = models.CharField(max_length=56, verbose_name='Название страны')

    def __str__(self):
        return self.name_country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class City(models.Model):
    """The model describes the city"""
    name_city = models.CharField(max_length=56, verbose_name='Название города')

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    """The model describes the street"""
    name_street = models.CharField(max_length=56, verbose_name='Название улицы')

    def __str__(self):
        return self.name_street

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'улицы'
