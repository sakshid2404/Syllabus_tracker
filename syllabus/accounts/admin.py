from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_staff', 'created_at']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('created_at',)}),
    )
    readonly_fields = ['created_at']
