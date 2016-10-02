# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_trabajador_estado'),
        ('producto', '0006_auto_20160322_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salidaspro',
            name='Trabajador',
        ),
        migrations.AddField(
            model_name='salidaspro',
            name='trabajador',
            field=models.ForeignKey(default='1', to='cliente.Trabajador'),
            preserve_default=False,
        ),
    ]
