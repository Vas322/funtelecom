# Generated by Django 3.1 on 2020-09-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='link_site',
            field=models.CharField(default=False, max_length=200, verbose_name='Ссылка на сайт'),
        ),
    ]