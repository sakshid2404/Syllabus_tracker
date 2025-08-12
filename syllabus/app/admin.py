from django.contrib import admin
from app.models import User, Syllabus, Subject, Chapter, Topic, Subtopic, StudySession, Revision, ProgressReport

class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','password','created_at')
    
class SyllabusAdmin(admin.ModelAdmin):
    list_display=('user','name','created_at')
    
class SubjectAdmin(admin.ModelAdmin):
    list_display=('name','syllabus','created_at','goal_hour')

class ChapterAdmin(admin.ModelAdmin):
    list_display=('title','subject')
    
class TopicAdmin(admin.ModelAdmin):
    list_display=('title','chapter')
    
class SubtopicAdmin(admin.ModelAdmin):
    list_display=('title','topic')

class StudySessionAdmin(admin.ModelAdmin):
    list_display=('user','topic','subtopic','date','duration_min','is_completed','created_at')

class RevisionAdmin(admin.ModelAdmin):
    list_display=('user','subject','topic','date','revision_type')

class ProgressReportAdmin(admin.ModelAdmin):
    list_display=('user','date','study_sessions','revisions','subjects','total_study_time','total_revision_time','created_at')
    

admin.site.register(User,UserAdmin)
admin.site.register(Syllabus,SyllabusAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Subtopic,SubtopicAdmin)
admin.site.register(StudySession,StudySessionAdmin)
admin.site.register(Revision,RevisionAdmin)
admin.site.register(ProgressReport,ProgressReportAdmin)