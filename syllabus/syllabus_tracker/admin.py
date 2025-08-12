from django.contrib import admin
from app.models import StudySession, Revision, ProgressReport


class StudySessionAdmin(admin.ModelAdmin):
    list_display=('user','topic','subtopic','date','duration_min','is_completed','created_at')


class RevisionAdmin(admin.ModelAdmin):
    list_display=('user','subject','topic','date','revision_type')


class ProgressReportAdmin(admin.ModelAdmin):
    list_display=('user','date','study_sessions','revisions','subjects','total_study_time','total_revision_time','created_at')
    

admin.site.register(StudySession,StudySessionAdmin)
admin.site.register(Revision,RevisionAdmin)
admin.site.register(ProgressReport,ProgressReportAdmin)