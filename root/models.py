from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="phone number", unique=True, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


