# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='Ci_Nit',
            field=models.PositiveIntegerField(unique=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='Telefono',
            field=models.PositiveIntegerField(max_length=15),
        ),
    ]
