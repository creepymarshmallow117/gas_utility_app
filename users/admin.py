from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email','first_name', 'last_name', 'is_support_staff','is_staff', 'is_active', 'panNumber')
    search_fields = ('username', 'email', 'panNumber')
    ordering = ('username',)
    list_filter = ('is_staff', 'is_support_staff')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_support_staff',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_support_staff',)}),
    )

