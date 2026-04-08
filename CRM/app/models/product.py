from django.db import models


class Product(models.Model):
    """产品模型 - 存储公司销售的产品或服务信息"""

    # 基础信息
    name = models.CharField(max_length=200, verbose_name='产品名称')
    description = models.TextField(blank=True, verbose_name='产品描述')
    category = models.CharField(max_length=100, blank=True, verbose_name='产品类别')
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='标准单价')
    stock_quantity = models.IntegerField(default=0, verbose_name='库存数量')

    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'
        ordering = ['category', 'name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """判断是否有库存"""
        return self.stock_quantity > 0