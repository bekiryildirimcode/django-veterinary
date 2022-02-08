from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'user'),
      (2, 'admin'),
    )
    role=models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,blank=True,default=1)
    
    class Meta:
        db_table='user'
        verbose_name="Users"
        verbose_name_plural="Users"

    def __str__(self):
        return self.username
