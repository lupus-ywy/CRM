from django.db import models
from django.contrib.auth.models import User


class Interaction(models.Model):
    """互动记录模型 - 记录与客户或线索的所有沟通历史"""

    # 互动类型选择
    TYPE_CHOICES = [
        ('phone', '电话'),
        ('email', '邮件'),
        ('meeting', '会议'),
        ('visit', '拜访'),
        ('wechat', '微信'),
        ('sms', '短信'),
        ('other', '其他'),
    ]

    # 关联对象（可选其一）
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, null=True, blank=True,
        related_name='interactions', verbose_name='客户'
    )
    contact = models.ForeignKey(
        'Contact', on_delete=models.CASCADE, null=True, blank=True,
        related_name='interactions', verbose_name='联系人'
    )
    lead = models.ForeignKey(
        'Lead', on_delete=models.CASCADE, null=True, blank=True,
        related_name='interactions', verbose_name='线索'
    )

    # 互动信息
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='interactions', verbose_name='跟进人'
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='互动类型')
    subject = models.CharField(max_length=200, verbose_name='互动主题')
    notes = models.TextField(verbose_name='沟通内容')
    interaction_time = models.DateTimeField(verbose_name='互动时间')

    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '互动记录'
        verbose_name_plural = '互动记录'
        ordering = ['-interaction_time']
        indexes = [
            models.Index(fields=['customer']),
            models.Index(fields=['contact']),
            models.Index(fields=['lead']),
            models.Index(fields=['user']),
            models.Index(fields=['type']),
            models.Index(fields=['interaction_time']),
        ]

    def __str__(self):
        return f'{self.get_type_display()} - {self.subject}'

    def clean(self):
        """确保至少关联了customer、contact或lead中的一个"""
        if not any([self.customer, self.contact, self.lead]):
            raise ValueError('必须关联客户、联系人或线索中的至少一个')