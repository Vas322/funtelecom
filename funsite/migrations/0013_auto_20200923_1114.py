# Generated by Django 3.1 on 2020-09-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0012_address_number_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(blank=True, help_text='Например, Адрес склада', max_length=50, verbose_name='Описание адреса'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_department',
            field=models.CharField(help_text='Например, Офис', max_length=50, verbose_name='Название подразделения'),
        ),
    ]
