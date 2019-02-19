# Generated by Django 2.1.5 on 2019-01-21 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.CharField(max_length=7)),
                ('typ', models.CharField(max_length=40)),
                ('cfa', models.CharField(blank=True, max_length=20)),
                ('rpTime', models.DateTimeField(auto_now_add=True)),
                ('faultDes', models.TextField(blank=True)),
                ('faultCon', models.TextField(blank=True)),
                ('costList', models.TextField(blank=True)),
                ('isComplete', models.BooleanField(default=False)),
                ('completeTime', models.DateTimeField(blank=True)),
                ('isCheck', models.BooleanField(default=False)),
                ('checkTime', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=15)),
                ('isRepairGuy', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='repairGuy',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='repairGuy', to='PCfix.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='PCfix.User'),
        ),
    ]
