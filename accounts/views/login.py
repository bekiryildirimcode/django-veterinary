from django.shortcuts import  render, redirect
from accounts.forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f" {username} olarak oturum açtınız.")
				return redirect("/")
			else:
				messages.error(request,"Geçersiz kullanıcı adı veya şifre.")
		else:
			messages.error(request,"Geçersiz kullanıcı adı veya şifre.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})