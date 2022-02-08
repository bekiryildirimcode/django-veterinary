from django import forms
from veterinary.models import OwnerModel
from django.contrib import messages
class NewOwnerForm(forms.ModelForm):
   
	class Meta:
		model = OwnerModel
		fields = ("name", "email", "phone", "address")

	def save(self, commit=True):
		user = super(NewOwnerForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user