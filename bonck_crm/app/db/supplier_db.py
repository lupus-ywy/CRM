from typing import Optional

from django.db.models import QuerySet

from bonck_crm.app.models import Supplier


class SupplierCRUD:
    """供应商CRUD操作"""

    @staticmethod
    def create(
        company_name: str,
        contact_person: str,
        phone: str,
        email: str,
        address: str = '',
        credit_rating: str = '',
        is_preferred: bool = False,
        active_flag: bool = True,
        website_url: str = ''
    ) -> Supplier:
        """创建新供应商"""
        return Supplier.objects.create(
            company_name=company_name,
            contact_person=contact_person,
            phone=phone,
            email=email,
            address=address,
            credit_rating=credit_rating,
            is_preferred=is_preferred,
            active_flag=active_flag,
            website_url=website_url
        )

    @staticmethod
    def get_by_id(supplier_id: int) -> Optional[Supplier]:
        """根据ID获取供应商"""
        try:
            return Supplier.objects.get(pk=supplier_id)
        except Supplier.DoesNotExist:
            return None

    @staticmethod
    def get_all() -> QuerySet[Supplier]:
        """获取所有供应商"""
        return Supplier.objects.all()

    @staticmethod
    def get_preferred() -> QuerySet[Supplier]:
        """获取首选供应商"""
        return Supplier.objects.filter(is_preferred=True)

    @staticmethod
    def get_active() -> QuerySet[Supplier]:
        """获取正在合作的供应商"""
        return Supplier.objects.filter(active_flag=True)

    @staticmethod
    def update(supplier_id: int, **kwargs) -> Optional[Supplier]:
        """更新供应商信息"""
        supplier = SupplierCRUD.get_by_id(supplier_id)
        if supplier:
            for key, value in kwargs.items():
                if hasattr(supplier, key):
                    setattr(supplier, key, value)
            supplier.save()
        return supplier

    @staticmethod
    def delete(supplier_id: int) -> bool:
        """删除供应商"""
        supplier = SupplierCRUD.get_by_id(supplier_id)
        if supplier:
            supplier.delete()
            return True
        return False