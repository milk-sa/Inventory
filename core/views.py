from rest_framework import viewsets
from .models import Product, StockEntry, Category, Supplier
from .serializers import (
    ProductSerializer,
    StockEntrySerializer,
    CategorySerializer,
    SupplierSerializer
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

class StockEntryViewSet(viewsets.ModelViewSet):
    queryset = StockEntry.objects.all().order_by('-date')
    serializer_class = StockEntrySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer
