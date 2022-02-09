from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUserModel
@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    model=CustomUserModel
    list_display=('username','email','role',)
    fieldsets = UserAdmin.fieldsets+ (
        ("Role",{
            "fields":["role"]
        }),
    )
