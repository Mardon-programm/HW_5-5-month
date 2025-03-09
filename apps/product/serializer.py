from rest_framework import serializers
from apps.product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'is_active', 'created_at'] 

# Сериализация Категории
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        filters = ['id', 'name', 'description']