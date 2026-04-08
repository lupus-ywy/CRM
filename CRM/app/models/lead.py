from django.db import models


class Lead(models.Model):
    """线索模型 - 管理销售流程的初始阶段"""

    # 联系方式类型选择
    CONTACT_TYPE_CHOICES = [
        ('phone', '手机号'),
        ('wechat', '微信号'),
        ('email', '邮箱'),
        ('other', '其他'),
    ]

    # 线索来源选择
    SOURCE_CHOICES = [
        ('website', '官网'),
        ('offline_event', '线下活动'),
        ('referral', '推荐'),
        ('advertisement', '广告'),
        ('social_media', '社交媒体'),
        ('exhibition', '展会'),
        ('cold_call', '陌生拜访'),
        ('other', '其他'),
    ]

    # 线索状态选择
    STATUS_CHOICES = [
        ('pending', '待联系'),
        ('contacted', '已联系'),
        ('converted', '已转化'),
        ('invalid', '无效'),
    ]

    # 基础信息
    name = models.CharField(max_length=100, verbose_name='线索姓名')
    contact_info = models.CharField(max_length=50, verbose_name='联系方式')
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES, default='phone', verbose_name='联系方式类型')
    source = models.CharField(max_length=30, choices=SOURCE_CHOICES, blank=True, verbose_name='线索来源')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='状态')

    # 跟进信息
    first_contact_date = models.DateField(null=True, blank=True, verbose_name='首次联系日期')
    last_contact_date = models.DateField(null=True, blank=True, verbose_name='最后沟通日期')

    # 备注
    notes = models.TextField(blank=True, verbose_name='备注')

    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '线索'
        verbose_name_plural = '线索'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['source']),
            models.Index(fields=['contact_info']),
        ]

    def __str__(self):
        return self.name