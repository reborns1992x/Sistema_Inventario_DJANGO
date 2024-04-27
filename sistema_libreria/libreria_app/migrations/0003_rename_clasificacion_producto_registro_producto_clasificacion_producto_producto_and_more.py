# Generated by Django 5.0.4 on 2024-04-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_app', '0002_remove_clasificacion_producto_nombre_clasificacion_producto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro_producto',
            old_name='clasificacion_Producto',
            new_name='clasificacion_Producto_Producto',
        ),
        migrations.AlterField(
            model_name='clasificacion_producto',
            name='lista_Clasificacion_Producto',
            field=models.CharField(choices=[('opcion1', 'Libros'), ('opcion2', 'Cuadernos'), ('opcion3', 'carpetas')], max_length=150),
        ),
    ]
