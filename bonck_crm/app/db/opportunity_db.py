from datetime import datetime
from typing import Optional

from django.contrib.auth.models import User
from django.db.models import QuerySet

from bonck_crm.app.models import Customer, Opportunity


class OpportunityCRUD:
    """销售机会CRUD操作"""

    @staticmethod
    def create(
        title: str,
        customer: Customer,
        stage: str = 'new_lead',
        amount: float = None,
        expected_close_date: datetime = None,
        assigned_to: Optional[User] = None
    ) -> Opportunity:
        """创建新销售机会"""
        return Opportunity.objects.create(
            title=title,
            customer=customer,
            stage=stage,
            amount=amount,
            expected_close_date=expected_close_date,
            assigned_to=assigned_to
        )

    @staticmethod
    def get_by_id(opportunity_id: int) -> Optional[Opportunity]:
        """根据ID获取销售机会"""
        try:
            return Opportunity.objects.get(pk=opportunity_id)
        except Opportunity.DoesNotExist:
            return None

    @staticmethod
    def get_by_customer(customer: Customer) -> QuerySet[Opportunity]:
        """获取客户的所有销售机会"""
        return Opportunity.objects.filter(customer=customer)

    @staticmethod
    def get_by_stage(stage: str) -> QuerySet[Opportunity]:
        """根据阶段获取销售机会"""
        return Opportunity.objects.filter(stage=stage)

    @staticmethod
    def update(opportunity_id: int, **kwargs) -> Optional[Opportunity]:
        """更新销售机会信息"""
        opportunity = OpportunityCRUD.get_by_id(opportunity_id)
        if opportunity:
            for key, value in kwargs.items():
                if hasattr(opportunity, key):
                    setattr(opportunity, key, value)
            opportunity.save()
        return opportunity

    @staticmethod
    def delete(opportunity_id: int) -> bool:
        """删除销售机会"""
        opportunity = OpportunityCRUD.get_by_id(opportunity_id)
        if opportunity:
            opportunity.delete()
            return True
        return False