from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from apps.dds import models, serializers

@extend_schema(tags=['Transaction'])
class Transaction(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.Transaction

@extend_schema(tags=['Type'])
class Type(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.Type

@extend_schema(tags=['Category'])
class Category(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category

@extend_schema(tags=['Subcategory'])
class Subcategory(viewsets.ModelViewSet):
    queryset = models.Subcategory.objects.all()
    serializer_class = serializers.SubCategory
