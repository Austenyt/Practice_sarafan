from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, SubCategory, Product, Cart
from .pagination import CategoryPagination, ProductPagination
from .serializers import CategorySerializer, SubcategorySerializer, ProductSerializer, CartSerializer, \
    CartProductSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class SubcategoryList(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        return SubCategory.objects.filter(category=category)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class CartAdd(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.create()
        cart.products.add(product)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.get(products__id=product_id)
        cart.products.add(product)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.get(products__id=product_id)
        cart.products.remove(product)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        cart_id = request.query_params.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        products = cart.products.all()
        total_quantity = 0
        total_price = 0
        for product in products:
            total_quantity += product.quantity
            total_price += product.price * product.quantity
        data = {
            'total_quantity': total_quantity,
            'total_price': total_price,
            'products': CartProductSerializer(products, many=True).data
        }
        return Response(data)


class CartClear(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        cart_id = request.query_params.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        cart.products.clear()
        return Response({'message': 'Cart cleared'})
