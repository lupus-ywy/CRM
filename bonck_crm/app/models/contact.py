from django.db import models


class Contact(models.Model):
    """联系人模型 - 记录客户方具体的对接人信息"""

    # 决策角色选择
    ROLE_CHOICES = [
        ('decision_maker', '决策者'),
        ('influencer', '影响者'),
        ('user', '使用者'),
        ('evaluator', '评估者'),
        ('gatekeeper', '守门人'),
        ('other', '其他'),
    ]

    # 关联客户
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='contacts',
        verbose_name='所属客户'
    )

    # 基本信息
    first_name = models.CharField(max_length=50, verbose_name='名字')
    last_name = models.CharField(max_length=50, verbose_name='姓氏')
    position = models.CharField(max_length=100, blank=True, verbose_name='职位')
    department = models.CharField(max_length=100, blank=True, verbose_name='部门')
    phone = models.CharField(max_length=50, blank=True, verbose_name='个人电话')
    email = models.EmailField(blank=True, verbose_name='个人邮箱')

    # 角色信息
    is_primary = models.BooleanField(default=False, verbose_name='是否为主要联系人')
    role_in_decision = models.CharField(max_length=30, choices=ROLE_CHOICES, blank=True, verbose_name='在采购决策中的角色')

    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = '联系人'
        ordering = ['-is_primary', 'last_name', 'first_name']
        indexes = [
            models.Index(fields=['customer']),
            models.Index(fields=['is_primary']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return f'{self.last_name}{self.first_name}'

    def save(self, *args, **kwargs):
        # 如果设置为主要联系人，则将同一客户的其他联系人的is_primary设为False
        if self.is_primary:
            Contact.objects.filter(customer=self.customer, is_primary=True).exclude(pk=self.pk).update(is_primary=False)
        super().save(*args, **kwargs)