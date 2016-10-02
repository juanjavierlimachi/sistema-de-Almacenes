# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_trabajador', models.CharField(max_length=150)),
                ('Apellidos', models.CharField(max_length=150)),
                ('Ci_Nit', models.IntegerField(unique=True, max_length=8)),
                ('Telefono', models.IntegerField()),
                ('Direccion', models.CharField(max_length=150)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
