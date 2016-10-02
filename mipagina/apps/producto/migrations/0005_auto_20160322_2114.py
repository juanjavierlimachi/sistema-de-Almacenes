# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_salidaspro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidaspro',
            name='fecha_registro',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
