from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from farmstack.inventory.models import InventoryItem, InventoryTransaction
from farmstack.sales.models import Customer, Sale
from farmstack.finance.models import FinanceRecord
from farmstack.practices.models import PlantingSchedule, CropRotation, PestControlActivity, IrrigationActivity
from farmstack.core.models import OfflineSyncRecord
from .serializers import (
    UserSerializer,
    InventoryItemSerializer, InventoryTransactionSerializer,
    CustomerSerializer, SaleSerializer,
    FinanceRecordSerializer,
    PlantingScheduleSerializer, CropRotationSerializer, PestControlActivitySerializer, IrrigationActivitySerializer,
    OfflineSyncRecordSerializer,
)
from farmstack.reports.utils import export_sales_excel, export_finance_pdf


User = get_user_model()


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if getattr(request.user, 'role', None) == 'admin' or request.user.is_superuser:
            return True
        owner = getattr(obj, 'owner', None) or getattr(obj, 'created_by', None)
        return owner == request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class OwnedModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    def perform_create(self, serializer):
        fields = serializer.Meta.model._meta.fields
        field_names = [f.name for f in fields]
        data = {}
        if 'owner' in field_names:
            data['owner'] = self.request.user
        if 'created_by' in field_names:
            data['created_by'] = self.request.user
        serializer.save(**data)

    def get_queryset(self):
        qs = super().get_queryset()
        if getattr(self.request.user, 'role', None) == 'admin' or self.request.user.is_superuser:
            return qs
        if hasattr(self.serializer_class.Meta.model, 'owner'):
            return qs.filter(owner=self.request.user)
        if hasattr(self.serializer_class.Meta.model, 'created_by'):
            return qs.filter(created_by=self.request.user)
        return qs.none()


class InventoryItemViewSet(OwnedModelViewSet):
    queryset = InventoryItem.objects.all().order_by('-updated_at')
    serializer_class = InventoryItemSerializer


class InventoryTransactionViewSet(OwnedModelViewSet):
    queryset = InventoryTransaction.objects.all().order_by('-date')
    serializer_class = InventoryTransactionSerializer


class CustomerViewSet(OwnedModelViewSet):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer


class SaleViewSet(OwnedModelViewSet):
    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer

    @action(detail=False, methods=['get'], url_path='export/excel')
    def export_excel(self, request):
        qs = self.get_queryset()
        return export_sales_excel(qs)


class FinanceRecordViewSet(OwnedModelViewSet):
    queryset = FinanceRecord.objects.all().order_by('-date')
    serializer_class = FinanceRecordSerializer

    @action(detail=False, methods=['get'], url_path='export/pdf')
    def export_pdf(self, request):
        qs = self.get_queryset()
        return export_finance_pdf(qs)


class PlantingScheduleViewSet(OwnedModelViewSet):
    queryset = PlantingSchedule.objects.all().order_by('-start_date')
    serializer_class = PlantingScheduleSerializer

    @action(detail=True, methods=['post'])
    def notify(self, request, pk=None):
        schedule = self.get_object()
        phone = request.user.phone_number
        if not phone:
            return Response({'detail': 'No phone number set.'}, status=400)
        from farmstack.core.tasks import send_planting_schedule_sms
        send_planting_schedule_sms.delay(phone, f"Reminder: Plant {schedule.crop_name} on {schedule.start_date}")
        return Response({'status': 'queued'})


class CropRotationViewSet(OwnedModelViewSet):
    queryset = CropRotation.objects.all().order_by('-created_at')
    serializer_class = CropRotationSerializer


class PestControlActivityViewSet(OwnedModelViewSet):
    queryset = PestControlActivity.objects.all().order_by('-date')
    serializer_class = PestControlActivitySerializer


class IrrigationActivityViewSet(OwnedModelViewSet):
    queryset = IrrigationActivity.objects.all().order_by('-date')
    serializer_class = IrrigationActivitySerializer


class OfflineSyncRecordViewSet(OwnedModelViewSet):
    queryset = OfflineSyncRecord.objects.all().order_by('-created_at')
    serializer_class = OfflineSyncRecordSerializer


# Create your views here.
