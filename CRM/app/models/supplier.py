from django.db import models


class Supplier(models.Model):
    """供应商模型 - 存储提供产品或服务的供应商信息"""

    # 基础信息
    company_name = models.CharField(max_length=200, verbose_name='供应商公司名称')
    contact_person = models.CharField(max_length=100, verbose_name='主要联系人姓名')
    phone = models.CharField(max_length=50, verbose_name='联系电话')
    email = models.EmailField(verbose_name='联系邮箱')
    address = models.CharField(max_length=500, blank=True, verbose_name='公司地址')
    credit_rating = models.CharField(max_length=20, blank=True, verbose_name='信用评级')
    is_preferred = models.BooleanField(default=False, verbose_name='是否为首选供应商')
    active_flag = models.BooleanField(default=True, verbose_name='是否正在合作')
    website_url = models.URLField(blank=True, verbose_name='供应商网站')

    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'
        ordering = ['-is_preferred', 'company_name']
        indexes = [
            models.Index(fields=['company_name']),
            models.Index(fields=['is_preferred']),
            models.Index(fields=['active_flag']),
        ]

    def __str__(self):
        return self.company_name