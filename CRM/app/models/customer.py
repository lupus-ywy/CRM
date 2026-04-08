from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """客户模型 - 存储已成交或已建立正式关系的客户信息"""

    # 客户类型选择
    CUSTOMER_TYPE_CHOICES = [
        ('enterprise', '企业'),
        ('individual', '个人'),
        ('government', '政府机构'),
        ('organization', '组织'),
    ]

    # 基础信息
    company_name = models.CharField(max_length=200, verbose_name='公司名称')
    industry = models.CharField(max_length=100, blank=True, verbose_name='所属行业')
    phone = models.CharField(max_length=50, blank=True, verbose_name='公司电话')
    email = models.EmailField(blank=True, verbose_name='公司邮箱')
    website = models.URLField(blank=True, verbose_name='公司网站')
    address = models.CharField(max_length=500, blank=True, verbose_name='公司地址')
    customer_type = models.CharField(max_length=30, choices=CUSTOMER_TYPE_CHOICES, default='enterprise', verbose_name='客户类型')
    credit_rating = models.CharField(max_length=20, blank=True, verbose_name='信用评级')

    # 负责人
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='owned_customers', verbose_name='负责人'
    )

    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['company_name']),
            models.Index(fields=['customer_type']),
            models.Index(fields=['owner']),
        ]

    def __str__(self):
        return self.company_name