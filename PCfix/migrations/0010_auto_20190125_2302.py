# Generated by Django 2.1.5 on 2019-01-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCfix', '0009_auto_20190125_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]