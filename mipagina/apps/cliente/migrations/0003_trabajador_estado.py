# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20160305_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='estado',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
