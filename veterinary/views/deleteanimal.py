from django.views.generic import DeleteView
from veterinary.models import AnimalModel
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    template_name='page/deleteconfirm.html'
    success_url = reverse_lazy("veterinary:owner")
    def get_queryset(self):
       animal=AnimalModel.objects.filter(slug=self.kwargs.get("slug"))
       return animal