from django.views.generic import DetailView 
from django.shortcuts import get_object_or_404
from veterinary.models import AnimalModel
from django.contrib.auth.mixins import LoginRequiredMixin

class AnimalDeteailView(LoginRequiredMixin, DetailView):

    template_name='page/detail_animal.html'
    context_object_name='animal'
    def get_object(self):
        return get_object_or_404(
            AnimalModel,slug=self.kwargs.get("slug")
        )
    