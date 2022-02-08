from multiprocessing import context
from django.shortcuts import render
from django.views import View
from veterinary.models import OwnerModel
from django.contrib.auth.mixins import LoginRequiredMixin
class OwnerView(LoginRequiredMixin,View):
    
    http_method_names=['get','post']
    def get(self,request):
       
        context={ 
            "owner":OwnerModel.objects.filter(user=request.user)
        }
        
        return render(request,'page/owner.html',context=context)