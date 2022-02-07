from multiprocessing import context
from django.shortcuts import render
from django.views import View
class HomeView(View):
    http_method_names=['get','post']
    def get(self,request):
        context={ }
        return render(request,'page/home.html',context=context)