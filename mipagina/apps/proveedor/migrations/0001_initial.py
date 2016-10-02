# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_Razon_Social', models.CharField(unique=True, max_length=200)),
                ('Nit', models.PositiveIntegerField(max_length=15)),
                ('Telefono', models.PositiveIntegerField(max_length=8)),
                ('Direccion', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
