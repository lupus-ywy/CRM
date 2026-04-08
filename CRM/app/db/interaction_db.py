from datetime import datetime
from typing import Optional

from django.contrib.auth.models import User
from django.db.models import QuerySet

from CRM.app.models import Customer, Contact, Lead, Interaction


class InteractionCRUD:
    """互动记录CRUD操作"""

    @staticmethod
    def create(
        type: str,
        subject: str,
        notes: str,
        interaction_time: datetime,
        customer: Customer = None,
        contact: Contact = None,
        lead: Lead = None,
        user: User = None
    ) -> Interaction:
        """创建新互动记录"""
        return Interaction.objects.create(
            type=type,
            subject=subject,
            notes=notes,
            interaction_time=interaction_time,
            customer=customer,
            contact=contact,
            lead=lead,
            user=user
        )

    @staticmethod
    def get_by_id(interaction_id: int) -> Optional[Interaction]:
        """根据ID获取互动记录"""
        try:
            return Interaction.objects.get(pk=interaction_id)
        except Interaction.DoesNotExist:
            return None

    @staticmethod
    def get_by_customer(customer: Customer) -> QuerySet[Interaction]:
        """获取客户的互动记录"""
        return Interaction.objects.filter(customer=customer)

    @staticmethod
    def get_by_lead(lead: Lead) -> QuerySet[Interaction]:
        """获取线索的互动记录"""
        return Interaction.objects.filter(lead=lead)

    @staticmethod
    def get_by_type(type: str) -> QuerySet[Interaction]:
        """根据类型获取互动记录"""
        return Interaction.objects.filter(type=type)

    @staticmethod
    def get_by_user(user: User) -> QuerySet[Interaction]:
        """获取用户的互动记录"""
        return Interaction.objects.filter(user=user)

    @staticmethod
    def update(interaction_id: int, **kwargs) -> Optional[Interaction]:
        """更新互动记录"""
        interaction = InteractionCRUD.get_by_id(interaction_id)
        if interaction:
            for key, value in kwargs.items():
                if hasattr(interaction, key):
                    setattr(interaction, key, value)
            interaction.save()
        return interaction

    @staticmethod
    def delete(interaction_id: int) -> bool:
        """删除互动记录"""
        interaction = InteractionCRUD.get_by_id(interaction_id)
        if interaction:
            interaction.delete()
            return True
        return False