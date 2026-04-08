from typing import Optional

from django.db.models import QuerySet

from bonck_crm.app.models import Product


class ProductCRUD:
    """产品CRUD操作"""

    @staticmethod
    def create(
        name: str,
        unit_price: float,
        description: str = '',
        category: str = '',
        stock_quantity: int = 0
    ) -> Product:
        """创建新产品"""
        return Product.objects.create(
            name=name,
            description=description,
            category=category,
            unit_price=unit_price,
            stock_quantity=stock_quantity
        )

    @staticmethod
    def get_by_id(product_id: int) -> Optional[Product]:
        """根据ID获取产品"""
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return None

    @staticmethod
    def get_all() -> QuerySet[Product]:
        """获取所有产品"""
        return Product.objects.all()

    @staticmethod
    def get_by_category(category: str) -> QuerySet[Product]:
        """根据类别获取产品"""
        return Product.objects.filter(category=category)

    @staticmethod
    def get_in_stock() -> QuerySet[Product]:
        """获取有库存的产品"""
        return Product.objects.filter(stock_quantity__gt=0)

    @staticmethod
    def update(product_id: int, **kwargs) -> Optional[Product]:
        """更新产品信息"""
        product = ProductCRUD.get_by_id(product_id)
        if product:
            for key, value in kwargs.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            product.save()
        return product

    @staticmethod
    def update_stock(product_id: int, quantity: int) -> Optional[Product]:
        """更新产品库存"""
        product = ProductCRUD.get_by_id(product_id)
        if product:
            product.stock_quantity = quantity
            product.save()
        return product

    @staticmethod
    def delete(product_id: int) -> bool:
        """删除产品"""
        product = ProductCRUD.get_by_id(product_id)
        if product:
            product.delete()
            return True
        return False