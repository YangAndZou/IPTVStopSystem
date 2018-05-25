# coding=utf-8
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding('utf8')


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
        verbose_name = '直播频道表'
        verbose_name_plural = '直播频道表'


class IPTVPlatform(models.Model):
    platform_name = models.CharField(max_length=128, verbose_name='平台名称')
    platform_desc = models.CharField(max_length=256, verbose_name='平台描述', null=True)

    class Meta:
        db_table = 'iptv_platform'
        verbose_name = '平台表'
        verbose_name_plural = '平台表'


class IPTVZone(models.Model):
    platform = models.ForeignKey(to=IPTVPlatform, verbose_name='平台')
    zone_name = models.CharField(max_length=256, verbose_name='区域名称')

    class Meta:
        db_table = 'iptv_zone'
        verbose_name = '区域表'
        verbose_name_plural = '区域表'


class IPTVZoneNode(models.Model):
    platform = models.ForeignKey(to=IPTVZone, verbose_name='区域')
    node_name = models.CharField(max_length=256, verbose_name='区域结点名称')

    class Meta:
        db_table = 'iptv_zone_node'
        verbose_name = '区域结点表'
        verbose_name_plural = '区域结点表'


class IPTVSystem(models.Model):
    operation_status = (
        ('0', '失败'),
        ('1', '成功')
    )
    router_group = models.ForeignKey(to=IPTVRouterGroup, verbose_name='控制路由组名称')
    platform = models.ForeignKey(to=IPTVPlatform, verbose_name='平台表')
    system_name = models.CharField(max_length=128, verbose_name='系统名称')
    status = models.SmallIntegerField(choices=operation_status, verbose_name='操作状态')
    router_ip = models.GenericIPAddressField(verbose_name='路由设备ip')
    system_manager = models.CharField(max_length=128, verbose_name='系统责任人', null=True)
    system_manage_room = models.CharField(max_length=128, verbose_name='责任科室', null=True)
    # TODO system_attr.. 是搜索框上提供的，功能未知
    system_attribute = models.CharField(max_length=128, verbose_name='系统属性')
    system_attribute_value = models.CharField(max_length=128, verbose_name='系统属性值')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        db_table = 'iptv_system'
        verbose_name = '路由系统表'
        verbose_name_plural = '路由系统表'


class IPTVProgramOperationLog(models.Model):
    program = models.ForeignKey(to=IPTVProgram, verbose_name='频道', related_name='iptv_program_operation_log')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        db_table = 'iptv_program_operation_log'
        verbose_name = '直播频道操作日志表'
        verbose_name_plural = '直播频道操作日志表'
