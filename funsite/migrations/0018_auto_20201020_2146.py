# Generated by Django 3.1 on 2020-10-20 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0017_auto_20201019_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name_city',
            field=models.CharField(max_length=56, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я0-9]+$')], verbose_name='Название города'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name_country',
            field=models.CharField(max_length=56, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Название страны'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='position_partner_on_market',
            field=models.CharField(help_text='Например, "Интегратор"', max_length=100, null=True, verbose_name='Позиция на рынке'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='target_registration',
            field=models.CharField(help_text='Например, покупка товаров оптом.', max_length=100, null=True, verbose_name='Цель заявки'),
        ),
        migrations.AlterField(
            model_name='street',
            name='name_street',
            field=models.CharField(help_text='Если в списке нет улицы, то внесите ее нажав на "+"', max_length=56, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я0-9]+$')], verbose_name='Название улицы'),
        ),
        migrations.DeleteModel(
            name='PositionInMarket',
        ),
        migrations.DeleteModel(
            name='TargetRegistrationPartner',
        ),
    ]
