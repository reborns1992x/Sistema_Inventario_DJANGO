# Generated by Django 5.0.4 on 2024-04-17 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_app', '0003_rename_clasificacion_producto_registro_producto_clasificacion_producto_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacion_producto',
            name='lista_Clasificacion_Producto',
            field=models.CharField(choices=[('opcion1', 'Libros'), ('opcion2', 'Cuadernos'), ('opcion3', 'carpetas')], default='SELECCIONE', max_length=150),
        ),
    ]
