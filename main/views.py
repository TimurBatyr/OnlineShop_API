import random

from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, ImageProduct, Collection, Colors, Cart, UserInfo
from .serializers import ProductSerializer, ImageSerializer, CollectionSerializer, ColorsSerializer, \
    SimilarProductSerializer, CollectionProductSerializer, NewProductSerializer, BestsellerSerializer, \
    NovinkiSerializer, CartSerializer, UserInfoSerializer, FavoriteSerializer


class Pagination(PageNumberPagination):
    """Пагинация"""
    def get_paginated_response(self, data):
        return super().get_paginated_response(data)


class SearchProductPagination(Pagination):
    """Пагинация для поиска товаров"""
    page_size = 12


class ProductViewSet(viewsets.ModelViewSet):
    """Товар"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    pagination_class = SearchProductPagination


@api_view(['GET'])
def filter(request, name):
    """Схожие товары по категории"""
    collection = Collection.objects.get(name=name)
    queryset = Product.objects.filter(collection=collection)[0:5]
    serializer = SimilarProductSerializer(queryset, many=True)
    return Response(serializer.data)


class ImagesViewSet(viewsets.ModelViewSet):
    """Фотографии для товара"""
    queryset = ImageProduct.objects.all()
    serializer_class = ImageSerializer


class CollectionPagination(Pagination):
    """Пагинация для Коллекции"""
    page_size = 8


class CollectionViewSet(viewsets.ModelViewSet):
    """Коллекция"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = CollectionPagination


class CollectionProductPagination(Pagination):
    """Колллекция для пагинации товаров"""
    page_size = 12


class CollectionProductView(generics.ListCreateAPIView):
    """Коллекция товаров"""
    queryset = Product.objects.all()
    pagination_class = CollectionProductPagination

    def list(self, request, pk):
        queryset = Product.objects.filter(collection=pk)
        serializer = CollectionProductSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class ColorsViewSet(viewsets.ModelViewSet):
    """Цвета товаров"""
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


@api_view(['GET'])
def new_products(request):
    """Новинки товаров"""
    new_products = Product.objects.all().filter(new=True)[0:5]
    serializer = NewProductSerializer(new_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def bestseller(request):
    """Хит продаж"""
    bestsellers = Product.objects.all().filter(bestseller=True)[0:8]
    serializer = BestsellerSerializer(bestsellers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def novinki(request):
    """Новинки на главной странице: пагинация 8шт, фронтэндщики сделают список по 4 шт"""
    novinki = Product.objects.all().filter(new=True)[0:8]
    serializer = NovinkiSerializer(novinki, many=True)
    return Response(serializer.data)


class CollectionMainPageViewSet(CollectionViewSet):
    """Коллекция на главной странице: пагинация 8шт, фронтэндщики сделают список по 4 шт"""
    pass


class CartViewSet(viewsets.ModelViewSet):
    """Корзина. Удаление при запросе Delete"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class UserInfoView(generics.CreateAPIView):
    """Информация Юзера"""
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """Избранное"""
    queryset = Product.objects.all()
    serializer_class = FavoriteSerializer
    pagination_class = CollectionProductPagination


@api_view(['GET'])
def search_product(request):
    item = []
    categories = Collection.objects.all().count()
    if categories >= 5:
        for i in Collection.objects.all().values_list('id')[0:5]:
            if Product.objects.all().filter(collection=i).first() is None:
                pass
            else:
                item.append(random.choice(Product.objects.all().filter(collection=i)))
    else:
        for i in Collection.objects.all().values_list('id')[0:categories]:
            if Product.objects.all().filter(collection=i).first() is None:
                pass
            else:
                item.append(random.choice(Product.objects.all().filter(collection=i)))
    serializer = SimilarProductSerializer(item, many=True)
    return Response(serializer.data)

