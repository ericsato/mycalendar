# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycal', '0001_squashed_0002_auto_20150715_0818'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Relationships',
            new_name='Relationship',
        ),
    ]
