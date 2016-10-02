# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_proveedor_estado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_categoria', models.CharField(unique=True, max_length=50)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cantidad', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_producto', models.CharField(unique=True, max_length=150)),
                ('Marca', models.CharField(max_length=50)),
                ('Precio_producto', models.FloatField()),
                ('Stock', models.IntegerField(default=0)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
                ('Categoria', models.ForeignKey(to='producto.Categoria')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ManyToManyField(to='producto.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(to='proveedor.Proveedor'),
            preserve_default=True,
        ),
    ]
