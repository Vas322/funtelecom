# Generated by Django 3.1 on 2020-10-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0020_auto_20201022_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailtosupport',
            name='serial_number',
            field=models.CharField(max_length=100, null=True, verbose_name='Серийный номер оборудования'),
        ),
    ]