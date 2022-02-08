from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('veterinary.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
