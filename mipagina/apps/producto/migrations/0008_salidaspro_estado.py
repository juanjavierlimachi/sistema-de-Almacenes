# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_auto_20160322_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='salidaspro',
            name='estado',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
