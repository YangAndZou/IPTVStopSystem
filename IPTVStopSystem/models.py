# coding=utf-8
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class IPTVProgram(models.Model):
    program_status = (
        ('1', '关停'),
        ('2', '正常')
    )
    program_name = models.CharField(max_length=128, verbose_name='频道名称')
    program_num = models.IntegerField(verbose_name='频道号')
    program_ip = models.CharField(max_length=128, verbose_name='频道ip')
    status = models.SmallIntegerField(choices=program_status, verbose_name='频道状态 1 关停 2 正常')

    # strategy = models.CharField(max_length=123)
    # program_desc = models.CharField(max_length=256, verbose_name='频道描述', null=True, blank=True)
    # router = models.ForeignKey(to="IPTVRouterGroup", verbose_name='控制路由组', related_name='iptv_program')

    class Meta:
        db_table = 'iptv_program'
        verbose_name = '直播频道表'
        verbose_name_plural = '直播频道表'


class IPTVCDNNode(models.Model):
    s = (
        ('1', '关停'),
        ('2', '正常')
    )
    platform = models.CharField(max_length=50, verbose_name='平台(中兴 / 华为)')
    city = models.CharField(max_length=128, verbose_name='所属地市')
    node_name = models.CharField(max_length=128, verbose_name='节点名称')
    status = models.SmallIntegerField(choices=s, verbose_name='状态')

    class Meta:
        db_table = 'iptv_cdn_node'
        verbose_name = 'CDN节点表'
        verbose_name_plural = 'CDN节点表'


class IPTVProgramOperationLog(models.Model):
    program = models.ForeignKey(to=IPTVProgram, verbose_name='频道', related_name='iptv_program_operation_log')
    content = models.TextField(verbose_name='操作内容')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        db_table = 'iptv_program_operation_log'
        verbose_name = '直播频道操作日志表'
        verbose_name_plural = '直播频道操作日志表'


class IPTVCDNOperationLog(models.Model):
    cdn = models.ForeignKey(to=IPTVCDNNode, verbose_name='CDN节点', related_name='iptv_cdn_operation_log')
    content = models.TextField(verbose_name='操作内容')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        db_table = 'iptv_cdn_operation_log'
        verbose_name = 'CDN操作日志表'
        verbose_name_plural = 'CDN操作日志表'


class IPTVProcessVerify(models.Model):
    o = (
        ('1', '关停'),
        ('2', '恢复')
    )
    t = (
        ('1', 'EPG关停'),
        ('2', '直播频道关停'),
        ('3', 'CDN关停')
    )
    s = (
        ('1', '审核中'),
        ('2', '未通过'),
        ('3', '已通过')
    )
    operation_type = models.SmallIntegerField(choices=o, verbose_name='操作 1 关停 2 恢复')
    process_type = models.SmallIntegerField(choices=t, verbose_name='操作类型 1:EPG关停 2:直播频道关停 3:CDN关停')
    operation_target = models.CharField(max_length=256, verbose_name='操作对象')
    status = models.SmallIntegerField(choices=s, verbose_name='审核状态，1:审核中 2:未通过 3:已通过')
    suggestion = models.TextField(verbose_name='意见', null=True, blank=True)

    class Meta:
        db_table = 'iptv_process_verify'
        verbose_name = '流程审批表'
        verbose_name_plural = '流程审批表'

# class IPTVRouterGroup(models.Model):
#     router_name = models.CharField(max_length=128, verbose_name='控制路由组名称')
#     router_desc = models.CharField(max_length=256, verbose_name='控制路由组描述', null=True, blank=True)
#
#     class Meta:
#         db_table = 'iptv_router_group'
#         verbose_name = '控制路由组表'
#         verbose_name_plural = '控制路由组表'
#
#
# class IPTVPlatform(models.Model):
#     platform_name = models.CharField(max_length=128, verbose_name='平台名称')
#     platform_desc = models.CharField(max_length=256, verbose_name='平台描述', null=True)
#
#     class Meta:
#         db_table = 'iptv_platform'
#         verbose_name = '平台表'
#         verbose_name_plural = '平台表'
#
# class IPTVZone(models.Model):
#     platform = models.ForeignKey(to=IPTVPlatform, verbose_name='平台')
#     zone_name = models.CharField(max_length=256, verbose_name='区域名称')
#
#     class Meta:
#         db_table = 'iptv_zone'
#         verbose_name = '区域表'
#         verbose_name_plural = '区域表'
#
#
# class IPTVZoneNode(models.Model):
#     platform = models.ForeignKey(to=IPTVZone, verbose_name='区域')
#     node_name = models.CharField(max_length=256, verbose_name='区域结点名称')
#
#     class Meta:
#         db_table = 'iptv_zone_node'
#         verbose_name = '区域结点表'
#         verbose_name_plural = '区域结点表'
#
#
# class IPTVSystem(models.Model):
#     operation_status = (
#         ('1', '失败'),
#         ('2', '成功')
#     )
#     router_group = models.ForeignKey(to=IPTVRouterGroup, verbose_name='控制路由组名称')
#     platform = models.ForeignKey(to=IPTVPlatform, verbose_name='平台表')
#     system_name = models.CharField(max_length=128, verbose_name='系统名称')
#     status = models.SmallIntegerField(choices=operation_status, verbose_name='操作结果')
#     router_ip = models.GenericIPAddressField(verbose_name='路由设备ip')
#     system_manager = models.CharField(max_length=128, verbose_name='系统责任人', null=True)
#     system_manage_room = models.CharField(max_length=128, verbose_name='责任科室', null=True)
#     system_attribute = models.CharField(max_length=128, verbose_name='系统属性')
#     system_attribute_value = models.CharField(max_length=128, verbose_name='系统属性值')
#     update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
#
#     class Meta:
#         db_table = 'iptv_system'
#         verbose_name = '路由系统表'
#         verbose_name_plural = '路由系统表'
