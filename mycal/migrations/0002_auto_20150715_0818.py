# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationship', models.CharField(default=b'friend', max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='date',
            name='relationship',
            field=models.ForeignKey(to='mycal.Relationships'),
            preserve_default=False,
        ),
    ]
