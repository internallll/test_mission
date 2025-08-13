from rest_framework import serializers

from apps.dds import models


class Transaction(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = "__all__"


class Category(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class SubCategory(serializers.ModelSerializer):
    class Meta:
        model = models.Subcategory
        fields = "__all__"


class Type(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = "__all__"
