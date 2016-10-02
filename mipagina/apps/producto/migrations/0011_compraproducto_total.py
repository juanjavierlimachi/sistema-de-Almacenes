# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0010_salidaspro_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='compraproducto',
            name='total',
            field=models.FloatField(default='150'),
            preserve_default=False,
        ),
    ]
