from rest_framework import serializers

from CRM.app.models.contact import Contact
from CRM.app.models.customer import Customer
from CRM.app.models.interaction import Interaction
from CRM.app.models.lead import Lead
from CRM.app.models.opportunity import Opportunity
from CRM.app.models.product import Product
from CRM.app.models.supplier import Supplier


class LeadSerializer(serializers.ModelSerializer):
    """线索Serializer"""
    class Meta:
        model = Lead
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': False},
            'contact_info': {'required': False},
        }


class CustomerSerializer(serializers.ModelSerializer):
    """客户Serializer"""
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'company_name': {'required': False},
        }


class ContactSerializer(serializers.ModelSerializer):
    """联系人Serializer"""
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class SupplierSerializer(serializers.ModelSerializer):
    """供应商Serializer"""
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    """产品Serializer"""
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class OpportunitySerializer(serializers.ModelSerializer):
    """销售机会Serializer"""
    class Meta:
        model = Opportunity
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'title': {'required': False},
            'customer': {'required': False},
        }


class InteractionSerializer(serializers.ModelSerializer):
    """互动记录Serializer"""
    class Meta:
        model = Interaction
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']