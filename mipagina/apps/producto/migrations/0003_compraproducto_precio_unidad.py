# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_compraproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compraproducto',
            name='Precio_unidad',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
    ]
