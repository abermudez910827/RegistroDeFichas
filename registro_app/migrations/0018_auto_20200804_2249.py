# Generated by Django 3.0.8 on 2020-08-05 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_app', '0017_auto_20200803_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qse',
            name='actividad',
            field=models.TextField(blank=True),
        ),
    ]
