# Generated by Django 2.2 on 2020-08-28 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200827_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectrequest',
            name='description',
        ),
    ]
