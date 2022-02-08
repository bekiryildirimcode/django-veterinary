from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from veterinary.models import OwnerModel
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from veterinary.forms import NewOwnerForm
class EditOwnerView(LoginRequiredMixin,View):
    
    http_method_names=['get','post']

    def get(self,request,slug):
        owner=get_object_or_404(OwnerModel,slug=slug,user=request.user)
        form=NewOwnerForm(instance=owner)
        
        context={ 
            "edit_form":form
        }
        
        return render(request,'page/edit_owner.html',context=context)

    def post(self,request,slug):
               owner=get_object_or_404(OwnerModel,slug=slug,user=request.user)
               form=NewOwnerForm(request.POST or None,instance=owner)
               if form.is_valid():
                   form.save()
                   messages.success(self.request, "Hayvan sahibi Güncellendi. " )
                   return redirect("veterinary:owner")
           
               else:
                    messages.success(self.request, "Hayvan sahibi Güncellenemedi. " )
                    return redirect("veterinary:editowner",slug=slug)
       
          