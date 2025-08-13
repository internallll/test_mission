from django.db import models

from apps.dds import consts


class Type(models.Model):
    name = models.CharField(
        "Тип операции", max_length=50, unique=True, choices=consts.TypeConsts
    )

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Категория
    """

    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, verbose_name="Тип операции"
    )
    name = models.CharField("Название категории", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.type} → {self.name}"


class Subcategory(models.Model):
    """
    Подкатегория
    """

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    name = models.CharField("Название подкатегории", max_length=100)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return f"{self.category} -> {self.name}"


class Transaction(models.Model):
    """ДДС"""

    status = models.CharField(verbose_name="Статус", choices=consts.StatusConsts)
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        verbose_name="Тип операции",
        null=True,
    )
    value = models.PositiveIntegerField(verbose_name="Количество средств", default=0)
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
