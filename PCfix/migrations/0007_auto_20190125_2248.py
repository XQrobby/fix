# Generated by Django 2.1.5 on 2019-01-25 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PCfix', '0006_auto_20190125_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='checkTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 48, 24, 608486, tzinfo=utc), verbose_name='验收时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='completeTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 48, 24, 608486, tzinfo=utc), verbose_name='完修时间'),
        ),
    ]
