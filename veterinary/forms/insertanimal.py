from django import forms
from veterinary.models import AnimalModel
from django.utils.translation import gettext_lazy as _
class NewAnimalForm(forms.ModelForm):

	class Meta:
		model = AnimalModel
		fields = ("kind", "genus", "name", "age","description",)
       
     
