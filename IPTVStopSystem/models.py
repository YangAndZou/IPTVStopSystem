# coding=utf-8
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class IPTVEPG(models.Model):
    s = (
        ('1', '关停'),
        ('2', '开启')
    )
    status = models.SmallIntegerField(choices=s, verbose_name='EPG状态')

    class Meta:
        db_table = 'iptv_epg'
        verbose_name = 'EPG表'
        verbose_name_plural = 'EPG表'


class IPTVProgram(models.Model):
    program_status = (
        ('1', '关停'),
        ('2', '正常')
    )
    # types = (
    #     ('sn', '省内'),
    #     ('gq', '高清'),
    #     ('ys', '央视'),
    #     ('ws', '卫视'),
    #     ('qt', '其他'),
    #     ('ff', '付费')
    # )
    # ip_types = (
    #     ('iptv', 'iptv'),
    #     ('iptv+', 'iptv+')
    # )
    # platform_type = (
    #     ('huawei', '华为'),
    #     ('ZTE', '中兴'),
    #     ('oldZTE', '旧版中兴')
    # )
    program_num = models.IntegerField(verbose_name='频道号')
    program_name = models.CharField(max_length=128, verbose_name='频道名称', null=True)
    program_type = models.CharField(max_length=30, verbose_name='频道类型', null=True)
    program_ip = models.CharField(max_length=256, verbose_name='频道ip', null=True)
    program_ip_type = models.CharField(verbose_name='ip地址类型', max_length=50, null=True)
    platform = models.CharField(max_length=30, verbose_name='平台类型', null=True)
    status = models.SmallIntegerField(choices=program_status, verbose_name='频道状态 1 关停 2 正常')

    def __str__(self):
        return self.program_name

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
    program = models.ForeignKey(to=IPTVProgram, verbose_name='频道', related_name='iptv_program_operation_log', null=True)
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


class IPTVAuthCode(models.Model):
    auth_code = models.CharField(max_length=256, verbose_name='授权码（加密）')

    class Meta:
        db_table = 'iptv_auth_code'
        verbose_name = '授权码表'
        verbose_name_plural = '授权码表'
