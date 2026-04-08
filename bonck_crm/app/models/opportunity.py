from django.db import models
from django.contrib.auth.models import User


class Opportunity(models.Model):
    """销售机会模型 - 跟踪具体的销售项目"""

    # 销售阶段选择
    STAGE_CHOICES = [
        ('new_lead', '新线索'),
        ('requirement', '需求确认'),
        ('proposal', '方案报价'),
        ('negotiation', '谈判中'),
        ('closed_won', '已成交'),
        ('closed_lost', '已丢失'),
    ]

    # 基础信息
    title = models.CharField(max_length=200, verbose_name='机会标题')
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='opportunities',
        verbose_name='客户'
    )
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='new_lead', verbose_name='销售阶段')
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='预计成交金额')
    expected_close_date = models.DateField(null=True, blank=True, verbose_name='预计成交日期')

    # 负责人
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='assigned_opportunities', verbose_name='负责人'
    )

    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '销售机会'
        verbose_name_plural = '销售机会'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['stage']),
            models.Index(fields=['customer']),
            models.Index(fields=['assigned_to']),
            models.Index(fields=['expected_close_date']),
        ]

    def __str__(self):
        return self.title