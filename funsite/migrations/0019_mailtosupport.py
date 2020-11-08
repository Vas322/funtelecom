# Generated by Django 3.1 on 2020-10-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0018_auto_20201020_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailToSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('sender', models.EmailField(max_length=150, verbose_name='Ваш email для ответа')),
                ('message', models.TextField(verbose_name='Детально опишите вашу задачу')),
            ],
        ),
    ]