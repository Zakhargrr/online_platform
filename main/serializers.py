from rest_framework import serializers

from main.models import NetworkNode, Product
from main.validators import FactoryValidator, RetailNetworkValidator, SoleProprietorValidator, DebtValidator, \
    ProhibitedFieldsValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        exclude = ('created_at',)
        validators = [
            FactoryValidator(category='category', supplier='supplier'),
            RetailNetworkValidator(category='category', supplier='supplier'),
            SoleProprietorValidator(category='category', supplier='supplier'),
            DebtValidator(category='category', debt='debt')
        ]


class NetworkNodeSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        exclude = ('created_at',)
        validators = [
            ProhibitedFieldsValidator(category='category', supplier='supplier', debt='debt')
        ]


class NetworkNodeSerializerListRetrieve(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)
    supplier = serializers.SerializerMethodField()

    @staticmethod
    def get_contacts(instance):
        return {"email": instance.email, "country": instance.country, "city": instance.city, "sreet": instance.street,
                "house_number": instance.house_number}

    @staticmethod
    def get_supplier(instance):
        if instance.supplier:
            return {"id": instance.supplier.id, "name": instance.supplier.name, "category": instance.supplier.category,
                    "city": instance.supplier.city}
        else:
            return {}

    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'category', 'contacts', 'products', 'supplier', 'debt', 'created_at']
