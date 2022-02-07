from django.contrib import admin
from veterinary.models import OwnerModel,AnimalModel

@admin.register(OwnerModel)
class OwnerAdmin(admin.ModelAdmin):
        model=OwnerModel
        model_name="owner"
        list_display=('name','email','phone','address','slug',)

@admin.register(AnimalModel)
class AnimalAdmin(admin.ModelAdmin):
        model=AnimalModel
        model_name="animal",
        list_display=('name','owner','kind','genus','owner',)     