# Generated by Django 3.1 on 2020-09-21 20:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import funsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0009_auto_20200912_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=56, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_country', models.CharField(max_length=56, verbose_name='Название страны')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_department', models.CharField(max_length=50, verbose_name='Название подразделения')),
                ('working_hours', models.CharField(help_text='Пример: С 9-00 до 18-00', max_length=30, verbose_name='Часы работы')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_street', models.CharField(max_length=56, verbose_name='Название улицы')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'улицы',
            },
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название Компании'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_news',
            field=models.ImageField(blank=True, upload_to=funsite.models.get_timestamp_path, verbose_name='Загрузить изображение* Изображение должнобыть квадратным для корректного отображения'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Склад', max_length=50, verbose_name='Описание адреса')),
                ('number_house', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)], verbose_name='Номер дома')),
                ('number_flat', models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)], verbose_name='Номер помещения')),
                ('number_office', models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)], verbose_name='Номер офиса')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funsite.city', verbose_name='Город')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funsite.country', verbose_name='Страна')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funsite.department', verbose_name='Название подразделения')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funsite.street', verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]
