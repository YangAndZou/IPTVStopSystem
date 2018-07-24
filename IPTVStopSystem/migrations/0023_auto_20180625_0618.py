# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-25 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPTVStopSystem', '0022_auto_20180625_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iptvcdnnode',
            name='status',
            field=models.SmallIntegerField(choices=[(1, b'\xe5\x85\xb3\xe5\x81\x9c'), (2, b'\xe6\xad\xa3\xe5\xb8\xb8')], verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='iptvepg',
            name='status',
            field=models.SmallIntegerField(choices=[(1, b'\xe5\x85\xb3\xe5\x81\x9c'), (2, b'\xe5\xbc\x80\xe5\x90\xaf')], verbose_name=b'EPG\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='iptvprogram',
            name='status',
            field=models.SmallIntegerField(choices=[(1, b'\xe5\x85\xb3\xe5\x81\x9c'), (2, b'\xe6\xad\xa3\xe5\xb8\xb8')], verbose_name=b'\xe9\xa2\x91\xe9\x81\x93\xe7\x8a\xb6\xe6\x80\x81 1 \xe5\x85\xb3\xe5\x81\x9c 2 \xe6\xad\xa3\xe5\xb8\xb8'),
        ),
    ]