# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0009_compraproducto_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='salidaspro',
            name='total',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
    ]
