from typing import Optional

from django.db.models import QuerySet

from CRM.app.models import Customer, Contact


class ContactCRUD:
    """联系人CRUD操作"""

    @staticmethod
    def create(
        customer: Customer,
        first_name: str,
        last_name: str,
        position: str = '',
        department: str = '',
        phone: str = '',
        email: str = '',
        is_primary: bool = False,
        role_in_decision: str = ''
    ) -> Contact:
        """创建新联系人"""
        return Contact.objects.create(
            customer=customer,
            first_name=first_name,
            last_name=last_name,
            position=position,
            department=department,
            phone=phone,
            email=email,
            is_primary=is_primary,
            role_in_decision=role_in_decision
        )

    @staticmethod
    def get_by_id(contact_id: int) -> Optional[Contact]:
        """根据ID获取联系人"""
        try:
            return Contact.objects.get(pk=contact_id)
        except Contact.DoesNotExist:
            return None

    @staticmethod
    def get_by_customer(customer: Customer) -> QuerySet[Contact]:
        """获取客户的所有联系人"""
        return Contact.objects.filter(customer=customer)

    @staticmethod
    def get_primary_contact(customer: Customer) -> Optional[Contact]:
        """获取客户的主要联系人"""
        try:
            return Contact.objects.get(customer=customer, is_primary=True)
        except Contact.DoesNotExist:
            return None

    @staticmethod
    def update(contact_id: int, **kwargs) -> Optional[Contact]:
        """更新联系人信息"""
        contact = ContactCRUD.get_by_id(contact_id)
        if contact:
            for key, value in kwargs.items():
                if hasattr(contact, key):
                    setattr(contact, key, value)
            contact.save()
        return contact

    @staticmethod
    def delete(contact_id: int) -> bool:
        """删除联系人"""
        contact = ContactCRUD.get_by_id(contact_id)
        if contact:
            contact.delete()
            return True
        return False