# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150301_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='image',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
