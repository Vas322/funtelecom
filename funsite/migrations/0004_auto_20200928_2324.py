# Generated by Django 3.1 on 2020-09-28 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funsite', '0003_partner_partner_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetRegistrationPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например, покупка товаров оптом.', max_length=100, verbose_name='Цель регистрации партнера')),
            ],
            options={
                'verbose_name': 'Цель регистрации',
                'verbose_name_plural': 'Цели регистрации',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='target_registration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funsite.targetregistrationpartner', verbose_name='Цель регистрации'),
        ),
    ]
