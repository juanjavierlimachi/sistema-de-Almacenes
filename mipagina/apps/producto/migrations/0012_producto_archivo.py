# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0011_compraproducto_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='archivo',
            field=models.FileField(default='img', upload_to=b'productos'),
            preserve_default=False,
        ),
    ]
