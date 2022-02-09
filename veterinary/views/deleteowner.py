from django.views.generic import DeleteView
from veterinary.models import OwnerModel
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse_lazy
from django.contrib import messages
class OwnerDeleteView(DeleteView):
    template_name='page/deleteconfirm.html'
    success_url = reverse_lazy("veterinary:owner")
    def get_queryset(self):
       
       owner=OwnerModel.objects.filter(slug=self.kwargs.get("slug"))
       return owner