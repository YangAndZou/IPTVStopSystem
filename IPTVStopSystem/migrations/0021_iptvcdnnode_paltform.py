# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-22 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPTVStopSystem', '0020_auto_20180622_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='iptvcdnnode',
            name='paltform',
            field=models.CharField(default=1, max_length=64, verbose_name=b'\xe5\xb9\xb3\xe5\x8f\xb0'),
            preserve_default=False,
        ),
    ]
