# Generated by Django 5.0.4 on 2024-05-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_pais_options_alter_cliente_pais_origen_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='pais'),
        ),
    ]