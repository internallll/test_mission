import logging

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from apps.dds import models, serializers

logger = logging.getLogger("webserver")


@extend_schema(tags=["Transaction"])
class Transaction(viewsets.ModelViewSet):
    """
    Ручки для работы с Транзакциями
    """
    try:
        queryset = models.Transaction.objects.all()
        serializer_class = serializers.Transaction
    except Exception:
        logger.exception("Ошибка при работе с Transaction")


@extend_schema(tags=["Type"])
class Type(viewsets.ModelViewSet):
    """Ручки для работы с Типами"""
    try:
        queryset = models.Type.objects.all()
        serializer_class = serializers.Type
    except Exception:
        logger.exception("Ошибка при работе с Type")


@extend_schema(tags=["Category"])
class Category(viewsets.ModelViewSet):
    """Ручки для работы с Категориями"""
    try:
        queryset = models.Category.objects.all()
        serializer_class = serializers.Category
    except Exception:
        logger.exception("Ошибка при работе с Category")


@extend_schema(tags=["Subcategory"])
class Subcategory(viewsets.ModelViewSet):
    """Ручки для работы с Подкатегориями"""
    try:
        queryset = models.Subcategory.objects.all()
        serializer_class = serializers.SubCategory
    except Exception:
        logger.exception("Ошибка при работе с Subcategory")
