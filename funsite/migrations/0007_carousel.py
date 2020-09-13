# Generated by Django 3.1 on 2020-09-06 11:27

from django.db import migrations, models
import funsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0006_news_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название новости в карусели')),
                ('text', models.TextField(verbose_name='Текст новости в карусели')),
                ('image_carousel', models.ImageField(blank=True, upload_to=funsite.models.get_timestamp_path, verbose_name='Загрузить изображение*. Рекомендуемые размеры: 1280х400 пикселей!')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка на новость, товар или сайт.')),
                ('index', models.IntegerField(verbose_name='Индекс приоритета отображения')),
            ],
            options={
                'verbose_name': 'Карусель',
                'verbose_name_plural': 'Карусели',
            },
        ),
    ]