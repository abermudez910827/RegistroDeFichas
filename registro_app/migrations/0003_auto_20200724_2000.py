# Generated by Django 3.0.8 on 2020-07-25 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_app', '0002_brigada_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brigada',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
