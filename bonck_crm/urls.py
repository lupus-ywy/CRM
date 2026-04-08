"""
URL configuration for bonck_crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bonck_crm.app.views import (
    LeadViewSet, CustomerViewSet, ContactViewSet,
    SupplierViewSet, ProductViewSet, OpportunityViewSet,
    InteractionViewSet
)

# 创建路由器并注册视图集
router = DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'opportunities', OpportunityViewSet)
router.register(r'interactions', InteractionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]