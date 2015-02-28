# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='nick',
            field=models.CharField(default='nick', unique=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='nick',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='lead',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
