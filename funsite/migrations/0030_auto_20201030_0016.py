# Generated by Django 3.1 on 2020-10-29 21:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0029_auto_20201030_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='department_street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='funsite.street', verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='accessmaplink',
            name='access_map_link',
            field=models.CharField(max_length=255, verbose_name='Ссылка на схему проезда'),
        ),
        migrations.AlterField(
            model_name='numberhouse',
            name='number_house',
            field=models.CharField(help_text='Если в списке нет номера дома, то внесите нажав на "+"', max_length=6, validators=[django.core.validators.RegexValidator(regex='^[0-9/]+$')], verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='numberoffice',
            name='number_office',
            field=models.CharField(help_text='Если в списке нет номера офиса, то внесите нажав на "+"', max_length=6, validators=[django.core.validators.RegexValidator(regex='^[0-9/]+$')], verbose_name='Номер офиса'),
        ),
        migrations.AlterField(
            model_name='street',
            name='name_street',
            field=models.CharField(help_text='Если в списке нет улицы, то внесите ее нажав на "+"', max_length=56, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я0-9]+$')], verbose_name='Название улицы'),
        ),
    ]
