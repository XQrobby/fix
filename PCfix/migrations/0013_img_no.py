# Generated by Django 2.1.5 on 2019-01-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCfix', '0012_auto_20190126_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='no',
            field=models.CharField(default='', max_length=7),
        ),
    ]
