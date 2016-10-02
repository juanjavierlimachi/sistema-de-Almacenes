# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20160309_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='estado',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
