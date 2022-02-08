from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
app_name = "accounts"   

urlpatterns = [
   
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]