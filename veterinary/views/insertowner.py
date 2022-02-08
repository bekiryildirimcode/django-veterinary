from multiprocessing import context
from django.shortcuts import render,redirect
from django.views import View
from veterinary.models import OwnerModel
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from veterinary.forms import NewOwnerForm
class InsertOwnerView(LoginRequiredMixin,View):
    
    http_method_names=['get','post']
    form = NewOwnerForm()
    def get(self,request):
        context={ 
            "insert_form":self.form
        }
        
        return render(request,'page/insert_owner.html',context=context)

    def post(self,request):
        form=NewOwnerForm(request.POST)
        if form.is_valid():
            owner = form.save(commit=False)
            owner.user=request.user
            owner.save()
            messages.success(self.request, "Hayvan sahibi Eklendi." )
            return redirect("veterinary:owner")
           
        else:
            messages.success(self.request, "Hayvan sahibi Eklenemedi." )
            return redirect("veterinary:insertowner")
       
          