# Generated by Django 3.0.8 on 2020-07-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brigada',
            name='nombre',
            field=models.CharField(default='', max_length=255),
        ),
    ]