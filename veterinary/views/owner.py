from multiprocessing import context
from django.shortcuts import render
from django.views import View
from veterinary.models import OwnerModel,AnimalModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
class OwnerView(LoginRequiredMixin,View):
    
    http_method_names=['get','post']
    def get(self,request):
        search=request.GET.get('search')
        owner=OwnerModel.objects.filter(user=request.user)
        if search:
            owner= owner.filter(
                Q(name__icontains=search) 
            )
           

        context={ 
            "owner":owner
        }
        
        return render(request,'page/owner.html',context=context)