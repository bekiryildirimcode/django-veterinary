from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
   
    role=models.BooleanField(default=False)
    class Meta:
        db_table='user'
        verbose_name="Users"
        verbose_name_plural="Users"

    def __str__(self):
        return self.username
