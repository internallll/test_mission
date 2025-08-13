from django.db import models


class StatusConsts(models.TextChoices):
    BUSINESS = "Бизнес"
    PERSONAL = "Личное"
    TAX = "Налог"
    ...


class TypeConsts(models.TextChoices):
    WITHDRAW = "Списание"
    ADD = "Пополнение"
    ...
