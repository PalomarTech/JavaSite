# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('coins', models.IntegerField(default=0)),
                ('posts', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
