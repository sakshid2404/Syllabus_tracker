<<<<<<< HEAD
=======
from django.contrib import admin
from app.models import  Syllabus
   
class SyllabusAdmin(admin.ModelAdmin):
    list_display=('user','name','created_at')
    



admin.site.register(Syllabus,SyllabusAdmin)
>>>>>>> 6a2beae6b079b7ab8e26ec8bcd9888130852c84b
