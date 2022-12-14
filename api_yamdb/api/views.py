from django_filters.rest_framework import DjangoFilterBackend
from reviews.models import Category, Genre, Title
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from serializers import CategorySerializer, GenreSerializer, TitleSerializer
from filters import TitleFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    # permission_classes
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    queryset = Title.objects.all()
