from django.db import models
from datetime import datetime
from os.path import splitext
from PIL import Image


def get_timestamp_path(instance, filename):
    """The function creates picture names based on the current date"""
    return "%s%s" % (datetime.now().timestamp(), splitext(filename)[1])


class Brand(models.Model):
    """The model describes the brand. Which will be display on the page."""
    name = models.CharField(max_length=200, verbose_name='Название бренда*')
    text = models.TextField(verbose_name='Описание бренда*')
    link_site = models.CharField(max_length=200, verbose_name='Ссылка на сайт')
    image_brand = models.ImageField(blank=True, upload_to=get_timestamp_path,
                                    verbose_name='Загрузить изображение*')

    def save(self):
        super().save()
        img = Image.open(self.image_brand.path)

        if img.height > 300 or img.width > 250:
            output_size_brand = (200, 200)
            img.thumbnail(output_size_brand)
            img.save(self.image_brand.path)

    class Meta:
        """Attribute allows you to use the plural form of 'Brands'"""
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class News(models.Model):
    """The model news. Which will display news on the page."""
    title = models.CharField(max_length=200, verbose_name='Название новости')
    text = models.TextField(verbose_name='Текст новости')
    image_news = models.ImageField(blank=True, upload_to=get_timestamp_path,
                                   verbose_name='Загрузить изображение*')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True,
                                        verbose_name='Дата публикации')

    def save(self):
        super().save()
        img = Image.open(self.image_news.path)

        if img.height > 300 or img.width > 300:
            output_size_news = (300, 300)
            img.thumbnail(output_size_news)
            img.save(self.image_news.path)

    class Meta:
        """Attribute allows you to use the plural form of 'News'"""
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
