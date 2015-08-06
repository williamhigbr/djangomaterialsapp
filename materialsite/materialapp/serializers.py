from models import Category
from models import ProductType
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
		class Meta:
			model = Category
			fields = ('id', 'name', 'description')


class ProductTypeSerializer(serializers.ModelSerializer):
		class Meta:
			model = ProductType
			fields = ('id', 'name', 'description', 'image')
