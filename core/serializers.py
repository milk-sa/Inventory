from rest_framework import serializers
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import EmployeeProfile


# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  
        # These are the fields included when sending category info in API

# Serializer for Supplier model
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_person', 'phone', 'email', 'address']

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    # Read-only nested serializers for related data
    category = CategorySerializer(read_only=True)   
    supplier = SupplierSerializer(read_only=True)
    
    # Write-only fields that accept category and supplier IDs on input
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),  # valid categories for writing
        source='category',                # points to the Product.category field
        write_only=True,                 # only used when creating/updating, not shown in output
        required=False                   # not mandatory to provide
    )
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        source='supplier',
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'quantity', 'price', 'low_stock_threshold',
            'category', 'supplier', 'category_id', 'supplier_id', 'created_at'
        ]
        

        
        
class StockEntrySerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = StockEntry
        fields = ['id', 'product', 'product_id', 'entry_type', 'quantity', 'date']

class EmployeeCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # Create EmployeeProfile with is_employee=True
        EmployeeProfile.objects.create(user=user, is_employee=True)
        return user
