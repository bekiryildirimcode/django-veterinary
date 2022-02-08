from django.contrib import admin
from django.urls import path
from veterinary.views import OwnerView
from veterinary.views import InsertOwnerView,EditOwnerView,InsertAnimalView

app_name="veterinary"
urlpatterns = [

    path('', OwnerView.as_view(),name="owner"),#Home page
    path('insertowner',InsertOwnerView.as_view(),name="insertowner"),
    path('editowner/<slug:slug>',EditOwnerView.as_view(),name="editowner"),
    path('insertanimal/<slug:slug>',InsertAnimalView.as_view(),name="insertanimal"),


    
]