# Generated by Django 3.0.8 on 2020-07-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_app', '0012_mesencurso_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesencurso',
            name='mes',
            field=models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril')]),
        ),
    ]
