# Generated by Django 2.2 on 2020-08-26 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200826_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Guide', verbose_name='guide'),
        ),
    ]
