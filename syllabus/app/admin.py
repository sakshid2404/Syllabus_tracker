from django.contrib import admin
from app.models import  Syllabus
   
class SyllabusAdmin(admin.ModelAdmin):
    list_display=('user','name','created_at')
    



admin.site.register(Syllabus,SyllabusAdmin)
