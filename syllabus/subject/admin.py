from django.contrib import admin
from subject.models import Subject, Chapter, Topic, Subtopic


class SubjectAdmin(admin.ModelAdmin):
    list_display=('name','syllabus','created_at','goal_hour')

class ChapterAdmin(admin.ModelAdmin):
    list_display=('title','subject')
    
class TopicAdmin(admin.ModelAdmin):
    list_display=('title','chapter')
    
class SubtopicAdmin(admin.ModelAdmin):
    list_display=('title','topic')
    
    
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Subtopic,SubtopicAdmin)