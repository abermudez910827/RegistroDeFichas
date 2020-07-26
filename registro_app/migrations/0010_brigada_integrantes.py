# Generated by Django 3.0.8 on 2020-07-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_app', '0009_zona_objetos'),
    ]

    operations = [
        migrations.AddField(
            model_name='brigada',
            name='integrantes',
            field=models.ManyToManyField(related_name='integrantes', to='registro_app.Persona', verbose_name='lista de integrantes'),
        ),
    ]
