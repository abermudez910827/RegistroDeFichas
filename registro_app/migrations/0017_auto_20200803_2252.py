# Generated by Django 3.0.8 on 2020-08-04 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_app', '0016_convenio_obra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenio',
            name='obra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_app.Obra'),
        ),
    ]
