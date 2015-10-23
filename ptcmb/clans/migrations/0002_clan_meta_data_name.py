# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clan_meta_data',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
