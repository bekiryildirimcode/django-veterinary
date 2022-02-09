from multiprocessing import context
from django.shortcuts import render
from django.views import View
from veterinary.models import OwnerModel,AnimalModel
from django.contrib.auth.mixins import LoginRequiredMixin
class AnimalView(LoginRequiredMixin,View):
    
    http_method_names=['get','post']
    def get(self,request,slug):
        owner=OwnerModel.objects.get(slug=slug)
        context={ 
            "animal":AnimalModel.objects.filter(owner=owner),
            "owner":OwnerModel.objects.filter(slug=slug)
        }
        
        return render(request,'page/animal.html',context=context)