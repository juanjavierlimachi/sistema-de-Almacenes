# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_proveedor_estado'),
        ('producto', '0003_compraproducto_precio_unidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalidasPro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Precio_unidad', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_registro', models.DateTimeField()),
                ('producto', models.ForeignKey(to='producto.Producto')),
                ('proveedor', models.ForeignKey(to='proveedor.Proveedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
