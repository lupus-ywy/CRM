from typing import Optional

from django.contrib.auth.models import User
from django.db.models import QuerySet

from bonck_crm.app.models import Customer


class CustomerCRUD:
    """客户CRUD操作"""

    @staticmethod
    def create(
        company_name: str,
        industry: str = '',
        phone: str = '',
        email: str = '',
        website: str = '',
        address: str = '',
        customer_type: str = 'enterprise',
        credit_rating: str = '',
        owner: Optional[User] = None
    ) -> Customer:
        """创建新客户"""
        return Customer.objects.create(
            company_name=company_name,
            industry=industry,
            phone=phone,
            email=email,
            website=website,
            address=address,
            customer_type=customer_type,
            credit_rating=credit_rating,
            owner=owner
        )

    @staticmethod
    def get_by_id(customer_id: int) -> Optional[Customer]:
        """根据ID获取客户"""
        try:
            return Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            return None

    @staticmethod
    def get_by_name(company_name: str) -> QuerySet[Customer]:
        """根据公司名称搜索客户"""
        return Customer.objects.filter(company_name__icontains=company_name)

    @staticmethod
    def get_all() -> QuerySet[Customer]:
        """获取所有客户"""
        return Customer.objects.all()

    @staticmethod
    def get_by_owner(user: User) -> QuerySet[Customer]:
        """获取指定负责人名下的客户"""
        return Customer.objects.filter(owner=user)

    @staticmethod
    def update(customer_id: int, **kwargs) -> Optional[Customer]:
        """更新客户信息"""
        customer = CustomerCRUD.get_by_id(customer_id)
        if customer:
            for key, value in kwargs.items():
                if hasattr(customer, key):
                    setattr(customer, key, value)
            customer.save()
        return customer

    @staticmethod
    def delete(customer_id: int) -> bool:
        """删除客户"""
        customer = CustomerCRUD.get_by_id(customer_id)
        if customer:
            customer.delete()
            return True
        return False