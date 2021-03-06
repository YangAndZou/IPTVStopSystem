# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-06 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPTVStopSystem', '0010_auto_20180604_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPTVAuthCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_code', models.CharField(max_length=256, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\xa0\x81\xef\xbc\x88\xe5\x8a\xa0\xe5\xaf\x86\xef\xbc\x89')),
            ],
            options={
                'db_table': 'iptv_auth_code',
                'verbose_name': '\u6388\u6743\u7801\u8868',
                'verbose_name_plural': '\u6388\u6743\u7801\u8868',
            },
        ),
        migrations.RemoveField(
            model_name='iptvprogram',
            name='program_num',
        ),
        migrations.AddField(
            model_name='iptvprogram',
            name='platform',
            field=models.CharField(choices=[(b'huawei', b'\xe5\x8d\x8e\xe4\xb8\xba'), (b'ZTE', b'\xe4\xb8\xad\xe5\x85\xb4'), (b'oldZTE', b'\xe6\x97\xa7\xe7\x89\x88\xe4\xb8\xad\xe5\x85\xb4')], default=1, max_length=30, verbose_name=b'\xe5\xb9\xb3\xe5\x8f\xb0\xe7\xb1\xbb\xe5\x9e\x8b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iptvprogram',
            name='program_ip_type',
            field=models.CharField(choices=[(b'iptv', b'iptv'), (b'iptv+', b'iptv+')], default=1, max_length=50, verbose_name=b'ip\xe5\x9c\xb0\xe5\x9d\x80\xe7\xb1\xbb\xe5\x9e\x8b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iptvprogram',
            name='program_type',
            field=models.CharField(choices=[(b'sn', b'\xe7\x9c\x81\xe5\x86\x85'), (b'gq', b'\xe9\xab\x98\xe6\xb8\x85'), (b'ys', b'\xe5\xa4\xae\xe8\xa7\x86'), (b'ws', b'\xe5\x8d\xab\xe8\xa7\x86'), (b'qt', b'\xe5\x85\xb6\xe4\xbb\x96'), (b'ff', b'\xe4\xbb\x98\xe8\xb4\xb9')], default=1, max_length=30, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93\xe7\xb1\xbb\xe5\x9e\x8b'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='iptvprocessverify',
            name='operation_type',
            field=models.SmallIntegerField(choices=[(b'1', b'\xe5\x85\xb3\xe5\x81\x9c'), (b'2', b'\xe6\x81\xa2\xe5\xa4\x8d')], verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb1\xbb\xe5\x9e\x8b 1 \xe5\x85\xb3\xe5\x81\x9c 2 \xe6\x81\xa2\xe5\xa4\x8d'),
        ),
        migrations.AlterField(
            model_name='iptvprocessverify',
            name='process_type',
            field=models.SmallIntegerField(choices=[(b'1', b'EPG\xe5\x85\xb3\xe5\x81\x9c'), (b'2', b'\xe7\x9b\xb4\xe6\x92\xad\xe9\xa2\x91\xe9\x81\x93\xe5\x85\xb3\xe5\x81\x9c'), (b'3', b'CDN\xe5\x85\xb3\xe5\x81\x9c')], verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe5\xaf\xb9\xe8\xb1\xa1\xe7\xb1\xbb\xe5\x9e\x8b 1:EPG\xe5\x85\xb3\xe5\x81\x9c 2:\xe7\x9b\xb4\xe6\x92\xad\xe9\xa2\x91\xe9\x81\x93\xe5\x85\xb3\xe5\x81\x9c 3:CDN\xe5\x85\xb3\xe5\x81\x9c'),
        ),
    ]
