# Generated by Django 2.1.5 on 2019-01-25 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PCfix', '0007_auto_20190125_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='checkTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='验收时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='completeTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='完修时间'),
        ),
    ]
