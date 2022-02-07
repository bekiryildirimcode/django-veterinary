from django.contrib import admin
from django.urls import path,include
from django.conf import settings
urlpatterns = [
    path('',include('veterinary.urls')),
    path('admin/', admin.site.urls),
]
