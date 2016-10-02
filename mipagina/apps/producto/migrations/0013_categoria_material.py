# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0012_producto_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='Material',
            field=models.CharField(default='Articulo', max_length=50),
            preserve_default=False,
        ),
    ]
