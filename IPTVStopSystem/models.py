# coding=utf-8
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class IPTVEPG(models.Model):
    """
    EPG模板表
    """
    s = (
        (0, '下线'),
        (1, '上线')
    )
    version = models.CharField(max_length=25, verbose_name='EPG模板版本')
    status = models.SmallIntegerField(choices=s, verbose_name='EPG状态', default=1)

    def __unicode__(self):
        return self.version

    class Meta:
        db_table = 'iptv_epg'
        verbose_name = 'EPG表'


class IPTVLiveProgram(models.Model):
    """
    直播频道表
    """
    s = (
        (0, '下线'),
        (1, '上线')
    )

    name = models.CharField(max_length=50, verbose_name='频道名称')
    status = models.SmallIntegerField(choices=s, verbose_name='频道状态', default=1)
    channel_id = models.CharField(max_length=25, verbose_name='频道名英文缩写')
    number = models.SmallIntegerField(verbose_name='频道号', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'iptv_live_program'
        verbose_name = '直播频道表'


class IPTVVOD(models.Model):
    """
    点播频道表
    """
    s = (
        (0, '下线'),
        (1, '上线')
    )
    name = models.CharField(max_length=50, verbose_name='已操作的点播频道名')
    status = models.SmallIntegerField(choices=s, verbose_name='点播频道状态', default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'iptv_vod'
        verbose_name = '点播频道表'


class IPTVRecommend(models.Model):
    """
    推荐位表
    """
    s = (
        (0, '下线'),
        (1, '上线')
    )

    desc = models.CharField(max_length=256, verbose_name='推荐描述', null=True, blank=True)
    picture_url = models.CharField(max_length=256, verbose_name='图片URL地址', null=True, blank=True)
    status = models.SmallIntegerField(choices=s, verbose_name='推荐位状态', default=1)
    version = models.CharField(max_length=25, verbose_name='模板版本')
    domain = models.CharField(max_length=25, verbose_name='当前页面所在域')
    postion_x = models.SmallIntegerField(verbose_name='横向编号')
    postion_y = models.IntegerField(verbose_name='纵向编号', null=True, blank=True)

    def __unicode__(self):
        return self.desc

    class Meta:
        db_table = 'iptv_recommend'
        verbose_name = '推荐位表'


class IPTVEPGLog(models.Model):
    """
    EPG操作日志记录表
    """
    log = models.ForeignKey(to='IPTVEPG', verbose_name='日志关联EPG的外键',
                            related_name='iptv_epg_log', on_delete=models.SET_NULL,
                            null=True, blank=True)
    content = models.CharField(max_length=100, verbose_name='操作内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'iptv_epg_log'
        verbose_name = 'EPG日志记录表'


class IPTVLiveProgramLog(models.Model):
    """
    直播频道操作日志记录表
    """
    log = models.ForeignKey(to='IPTVLiveProgram', verbose_name='日志关联直播的外键',
                            related_name='iptv_live_program_log', on_delete=models.SET_NULL,
                            null=True, blank=True)
    content = models.CharField(max_length=100, verbose_name='操作内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'iptv_live_program_log'
        verbose_name = '直播频道操作日志记录表'


class IPTVVODLog(models.Model):
    """
       点播频道操作日志记录表
       """
    log = models.ForeignKey(to='IPTVVOD', verbose_name='日志关联点播的外键',
                            related_name='iptv_vod_log', on_delete=models.SET_NULL,
                            null=True, blank=True)
    content = models.CharField(max_length=100, verbose_name='操作内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'iptv_vod_log'
        verbose_name = '点播频道操作日志记录表'


class IPTVRecommendLog(models.Model):
    log = models.ForeignKey(to='IPTVRecommend', verbose_name='日志关联推荐位的外键',
                            related_name='iptv_recommend_log', on_delete=models.SET_NULL,
                            null=True, blank=True)
    content = models.CharField(max_length=100, verbose_name='操作内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'iptv_recommend_log'
        verbose_name = '点播频道操作日志记录表'
