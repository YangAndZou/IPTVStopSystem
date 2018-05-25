# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class IPTVRouterGroup(models.Model):
    router_name = models.CharField(max_length=128, verbose_name='控制路由组名称')
    router_desc = models.CharField(max_length=256, verbose_name='控制路由组描述', null=True, blank=True)

    class Meta:
        db_table = 'iptv_router_group'
        verbose_name = '控制路由组表'
        verbose_name_plural = '控制路由组表'


class IPTVProgram(models.Model):
    program_status = (
        ('0', 'off'),
        ('1', 'on')
    )
    program_name = models.CharField(max_length=128, verbose_name='频道名称')
    program_desc = models.CharField(max_length=256, verbose_name='频道描述', null=True, blank=True)
    router = models.ForeignKey(to=IPTVRouterGroup, verbose_name='控制路由组', related_name='iptv_program')
    status = models.SmallIntegerField(choices=program_status, verbose_name='频道状态 0 关闭 1 开启')
    # TODO 策略id？
    strategy = models.CharField(max_length=123)

    class Meta:
        db_table = 'iptv_program'
        verbose_name = '频道表'
        verbose_name_plural = '频道表'


class IPTVProgramOperationLog(models.Model):
    program = models.ForeignKey(to=IPTVProgram, verbose_name='频道', related_name='iptv_program_operation_log')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        db_table = 'iptv_program_operation_log'
        verbose_name = '频道操作日志表'
        verbose_name_plural = '频道操作日志表'

