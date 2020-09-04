# Generated by Django 3.1 on 2020-09-03 21:32

from django.db import migrations, models
import funsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0004_auto_20200904_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название новости')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('image_news', models.ImageField(blank=True, upload_to=funsite.models.get_timestamp_path, verbose_name='Загрузить изображение*')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AlterField(
            model_name='brand',
            name='image_brand',
            field=models.ImageField(blank=True, upload_to=funsite.models.get_timestamp_path, verbose_name='Загрузить изображение*'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название бренда*'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='text',
            field=models.TextField(verbose_name='Описание бренда*'),
        ),
    ]
