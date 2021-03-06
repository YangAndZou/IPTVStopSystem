# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-22 01:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('IPTVStopSystem', '0019_auto_20180615_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iptvcdnnode',
            name='node_name',
        ),
        migrations.RemoveField(
            model_name='iptvcdnnode',
            name='platform',
        ),
        migrations.AddField(
            model_name='iptvcdnnode',
            name='device_name',
            field=models.CharField(default=datetime.datetime(2018, 6, 22, 1, 13, 26, 189830, tzinfo=utc), max_length=64, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x90\x8d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iptvcdnnode',
            name='ip',
            field=models.CharField(default=1, max_length=128, verbose_name=b'ip'),
            preserve_default=False,
        ),
    ]
