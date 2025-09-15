from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    InventoryItemViewSet, InventoryTransactionViewSet,
    CustomerViewSet, SaleViewSet,
    FinanceRecordViewSet,
    PlantingScheduleViewSet, CropRotationViewSet, PestControlActivityViewSet, IrrigationActivityViewSet,
    OfflineSyncRecordViewSet,
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('inventory/items', InventoryItemViewSet)
router.register('inventory/transactions', InventoryTransactionViewSet)
router.register('sales/customers', CustomerViewSet)
router.register('sales/sales', SaleViewSet)
router.register('finance/records', FinanceRecordViewSet)
router.register('practices/planting', PlantingScheduleViewSet)
router.register('practices/rotation', CropRotationViewSet)
router.register('practices/pest', PestControlActivityViewSet)
router.register('practices/irrigation', IrrigationActivityViewSet)
router.register('offline/sync', OfflineSyncRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', __import__('farmstack.api.auth_views', fromlist=['']).LoginView.as_view(), name='api-login'),
]

