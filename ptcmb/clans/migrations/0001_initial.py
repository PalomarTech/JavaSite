# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clan_Meta_Data',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('coins', models.IntegerField(default=0)),
                ('posts', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
            ],
        ),
    ]
