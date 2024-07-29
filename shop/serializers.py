from rest_framework import serializers
from .models import Category, SubCategory, Product, Cart


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'slug', 'image', 'category')


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'image', 'subcategories')


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'category', 'subcategory', 'price', 'description', 'images')

    def get_images(self, obj):
        return [image.url for image in obj.image_1.all()]


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'category', 'subcategory', 'price', 'description', 'images')


class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'products', 'created_at')
