# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_memberdata_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberdata',
            name='password',
        ),
    ]
