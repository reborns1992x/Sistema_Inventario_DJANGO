# Generated by Django 5.0.4 on 2024-04-18 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_app', '0008_alter_registro_producto_clasificacion_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_producto',
            name='imagen_Producto',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_producto/'),
        ),
        migrations.AlterField(
            model_name='clasificacionproducto',
            name='lista_Clasificacion_Producto',
            field=models.CharField(choices=[('1', 'SELECCIONE'), ('2', 'Libros'), ('3', 'Cuadernos'), ('4', 'carpetas')], default='1', max_length=150),
        ),
        migrations.AlterField(
            model_name='registro_producto',
            name='clasificacion_Producto',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='libreria_app.clasificacionproducto'),
        ),
    ]
