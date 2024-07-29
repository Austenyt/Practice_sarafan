from django.urls import path, include
from rest_framework import routers

from shop.views import CategoryList, SubcategoryList, ProductList, CartList, CartAdd, CartUpdate, CartDelete, \
    CartDetail, CartClear

router = routers.DefaultRouter()
router.register(r'categories', CategoryList, basename='category')
router.register(r'subcategories', SubcategoryList, basename='subcategory')
router.register(r'products', ProductList, basename='product')
router.register(r'products', CartList, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('cart/add/', CartAdd.as_view(), name='cart_add'),
    path('cart/update/', CartUpdate.as_view(), name='cart_update'),
    path('cart/delete/', CartDelete.as_view(), name='cart_delete'),
    path('cart/detail/', CartDetail.as_view(), name='cart_detail'),
    path('cart/clear/', CartClear.as_view(), name='cart_clear'),
]
