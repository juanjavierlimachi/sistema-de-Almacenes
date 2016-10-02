# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20160322_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salidaspro',
            old_name='proveedor',
            new_name='Trabajador',
        ),
    ]
