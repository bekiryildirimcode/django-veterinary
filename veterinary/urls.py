from django.contrib import admin
from django.urls import path
from veterinary.views import HomeView
urlpatterns = [
    path('', HomeView.as_view(),name="homepage"),

]