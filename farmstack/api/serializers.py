from rest_framework import serializers
from django.contrib.auth import get_user_model
from farmstack.inventory.models import InventoryItem, InventoryTransaction
from farmstack.sales.models import Customer, Sale, SaleItem
from farmstack.finance.models import FinanceRecord
from farmstack.practices.models import PlantingSchedule, CropRotation, PestControlActivity, IrrigationActivity
from farmstack.core.models import OfflineSyncRecord


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number', 'preferred_language']


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']


class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['id', 'product_name', 'quantity', 'unit_price', 'line_total']
        read_only_fields = ['line_total']


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id', 'customer', 'date', 'total_amount', 'note', 'created_by', 'created_at', 'items']
        read_only_fields = ['created_by', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        sale = Sale.objects.create(**validated_data)
        for item in items_data:
            SaleItem.objects.create(sale=sale, **item)
        return sale


class FinanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceRecord
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']


class PlantingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantingSchedule
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']


class CropRotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropRotation
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']


class PestControlActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PestControlActivity
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']


class IrrigationActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationActivity
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']


class OfflineSyncRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineSyncRecord
        fields = ['id', 'payload', 'status', 'created_at']

