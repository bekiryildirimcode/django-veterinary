from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from veterinary.models import AnimalModel,OwnerModel
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from veterinary.forms import NewAnimalForm
class EditAnimalView(LoginRequiredMixin,View):
    
    http_method_names=['get','post']

    def get(self,request,slug):
        animal=get_object_or_404(AnimalModel,slug=slug)
        form=NewAnimalForm(instance=animal)
        
        context={ 
            "edit_form":form
        }
        
        return render(request,'page/edit_animal.html',context=context)

    def post(self,request,slug):
               animal=get_object_or_404(AnimalModel,slug=slug)
               owner=OwnerModel.objects.get(owner=animal)
               form=NewAnimalForm(request.POST or None,instance=animal)
               if form.is_valid():
                   form.save()
                   messages.success(self.request, "Hayvan  Güncellendi. " )
                   return redirect("veterinary:animal",slug=owner.slug)
           
               else:
                    messages.success(self.request, "Hayvan  Güncellenemedi. " )
                    return redirect("veterinary:editowner",slug=owner.slug)
       
          