from django.db import models
from autoslug import AutoSlugField
from .Owner import OwnerModel
class AnimalModel(models.Model):
    owner=models.ForeignKey(OwnerModel,on_delete=models.CASCADE,related_name="owner",null=True)
    kind= models.CharField(max_length=50,null=True)
    genus= models.CharField(max_length=50,null=True)
    name= models.CharField(max_length=70,null=True)
    slug = AutoSlugField(populate_from='name')
    age=models.IntegerField(blank=True,unique=False)
    description=models.TextField(unique=False,null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name="Animal"
        verbose_name = 'Animal'

    def __str__(self):
        return self.name