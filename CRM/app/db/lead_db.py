from typing import Optional

from django.db.models import QuerySet

from CRM.app.models import Lead, Customer


class LeadCRUD:
    """线索CRUD操作"""

    @staticmethod
    def create(
        name: str,
        contact_info: str,
        contact_type: str = 'phone',
        source: str = '',
        notes: str = ''
    ) -> Lead:
        """创建新线索"""
        return Lead.objects.create(
            name=name,
            contact_info=contact_info,
            contact_type=contact_type,
            source=source,
            notes=notes
        )

    @staticmethod
    def get_by_id(lead_id: int) -> Optional[Lead]:
        """根据ID获取线索"""
        try:
            return Lead.objects.get(pk=lead_id)
        except Lead.DoesNotExist:
            return None

    @staticmethod
    def get_all() -> QuerySet[Lead]:
        """获取所有线索"""
        return Lead.objects.all()

    @staticmethod
    def get_by_status(status: str) -> QuerySet[Lead]:
        """根据状态获取线索"""
        return Lead.objects.filter(status=status)

    @staticmethod
    def update(lead_id: int, **kwargs) -> Optional[Lead]:
        """更新线索信息"""
        lead = LeadCRUD.get_by_id(lead_id)
        if lead:
            for key, value in kwargs.items():
                if hasattr(lead, key):
                    setattr(lead, key, value)
            lead.save()
        return lead

    @staticmethod
    def delete(lead_id: int) -> bool:
        """删除线索"""
        lead = LeadCRUD.get_by_id(lead_id)
        if lead:
            lead.delete()
            return True
        return False

    @staticmethod
    def convert_to_customer(lead_id: int, company_name: str) -> Optional[Customer]:
        """将线索转化为客户"""
        lead = LeadCRUD.get_by_id(lead_id)
        if lead:
            customer = Customer.objects.create(
                company_name=company_name,
                owner=lead.assigned_to if hasattr(lead, 'assigned_to') else None
            )
            lead.status = 'converted'
            lead.save()
            return customer
        return None