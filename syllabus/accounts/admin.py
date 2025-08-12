from django.contrib import admin
from app.models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','password','created_at')
    
admin.site.register(User,UserAdmin)