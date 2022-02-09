from django.contrib import admin
from django.urls import path
from veterinary.views import OwnerView
from veterinary.views import( InsertOwnerView,EditOwnerView,InsertAnimalView,AnimalView,EditAnimalView,
AnimalDeteailView ,AnimalDeleteView,OwnerDeleteView)

app_name="veterinary"
urlpatterns = [

    path('', OwnerView.as_view(),name="owner"),#Home page
    path('insertowner',InsertOwnerView.as_view(),name="insertowner"),
    path('editowner/<slug:slug>',EditOwnerView.as_view(),name="editowner"),
    path('animal/<slug:slug>',AnimalView.as_view(),name="animal"),
    path('insertanimal/<slug:slug>',InsertAnimalView.as_view(),name="insertanimal"),
    path('editanimal/<slug:slug>',EditAnimalView.as_view(),name="editanimal"),
    path('detailanimal/<slug:slug>',AnimalDeteailView.as_view(),name="detailanimal"),
    path('deleteowner/<slug:slug>',AnimalDeleteView.as_view(),name="animaldelete"),
    path('deleteanimal/<slug:slug>',OwnerDeleteView.as_view(),name="ownerdelete"),

    
]