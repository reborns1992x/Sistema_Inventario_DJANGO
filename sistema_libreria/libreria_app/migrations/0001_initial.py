# Generated by Django 5.0.4 on 2024-04-15 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clasificacion_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Clasificacion_Producto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='registro_Producto',
            fields=[
                ('id_Producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Producto', models.CharField(max_length=100)),
                ('cantidad_Producto', models.IntegerField(default=0)),
                ('costo_Producto', models.IntegerField(default=0)),
                ('descripcion_Producto', models.CharField(max_length=100)),
                ('clasificacion_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria_app.clasificacion_producto')),
            ],
        ),
    ]
