# Generated by Django 2.2 on 2020-08-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200824_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/', verbose_name='file'),
        ),
    ]
