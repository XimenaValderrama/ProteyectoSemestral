# Generated by Django 4.0.4 on 2022-05-16 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carrito',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=40)),
                ('precio_producto', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='carrito')),
            ],
            options={
                'db_table': 'db_carrito',
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_tipo_producto',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.IntegerField()),
                ('pnombre', models.CharField(max_length=20)),
                ('snombre', models.CharField(max_length=20)),
                ('appaterno', models.CharField(max_length=20)),
                ('apmaterno', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=90)),
                ('codigo_postal', models.IntegerField()),
                ('telefono1', models.IntegerField()),
                ('contrasena', models.CharField(max_length=20)),
                ('imagen_usu', models.ImageField(null=True, upload_to='perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('create_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoproducto')),
            ],
            options={
                'db_table': 'db_producto',
            },
        ),
    ]