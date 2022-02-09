from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUserModel

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUserModel
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user