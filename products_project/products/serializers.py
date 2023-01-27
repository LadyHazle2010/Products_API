from rest_framework import serializers
from .models import Products

class Productsserializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity']