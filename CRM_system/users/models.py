from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель потенциального клиента
    """
    surname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)


