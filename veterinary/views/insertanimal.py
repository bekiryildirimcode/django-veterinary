from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from veterinary.models import AnimalModel,OwnerModel
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from veterinary.forms import NewAnimalForm
class InsertAnimalView(LoginRequiredMixin,View):
  
    
    http_method_names=['get','post']

    def get(self,request,slug):
        
       
        form=NewAnimalForm() 
        
        context={ 
            "insert_form":form
        }
        
        return render(request,'page/insert_animal.html',context=context)

    def post(self,request,slug):
        owner=OwnerModel.objects.get(slug=slug)
        form=NewAnimalForm(request.POST)
        if form.is_valid():
          animal = form.save(commit=False)
          animal.owner=owner
          animal.save()
          messages.success(self.request, "Hayvan  Eklendi." )
          return redirect("veterinary:owner")
           
        else:
            messages.success(self.request, "Hayvan  Eklenemedi." )
            return redirect("veterinary:insertowner")
       
          
          