from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


class CategoryFilter(PageNumberPagination):
    class Meta:
        model = Category
        fields = ['name']


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_set = CategoryFilter
    pagination_class = PageNumberPagination


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    pagination_class = PageNumberPagination
