from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity']



# from rest_framework import serializers
# from .models import Car

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = ['id', 'make', 'model', 'year', 'price']