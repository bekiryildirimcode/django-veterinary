from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
class OwnerModel(models.Model):
    user = models.ForeignKey('accounts.CustomUserModel',on_delete=models.CASCADE,related_name="user",null=True)
    name= models.CharField(max_length=50,null=True)
    slug = AutoSlugField(populate_from='name')
    email=models.EmailField(max_length=70,blank=True,unique=True)
    phone = models.CharField(max_length=17, unique=False)
    address=models.TextField(unique=False,null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

 
    class Meta:
        verbose_name="Owner"
        verbose_name = 'Owner'

    def __str__(self):
        return self.name