# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarfront', '0002_auto_20150727_1410'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='user_profile',
        ),
    ]
