from rest_framework import serializers

from apps.dds import models


class Type(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = "__all__"


class SubCategory(serializers.ModelSerializer):
    class Meta:
        model = models.Subcategory
        fields = "__all__"


class Category(serializers.ModelSerializer):
    subcategories = SubCategory(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = "__all__"


class Transaction(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = "__all__"

    def validate(self, data):
        if data["category"].type != data["type"]:
            raise serializers.ValidationError(
                "Выбранная категория не принадлежит выбранному типу операции"
            )

        return data
