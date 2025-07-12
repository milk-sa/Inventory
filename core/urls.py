from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockEntryViewSet, CategoryViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stock-entries', StockEntryViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
