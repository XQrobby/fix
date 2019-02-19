# Generated by Django 2.1.5 on 2019-01-30 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PCfix', '0021_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receiveTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='接单时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='处理中', max_length=4),
        ),
    ]
