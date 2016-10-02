# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_salidaspro_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='compraproducto',
            name='estado',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
