from django.contrib import admin
from syllabus_tracker.models import StudySession, Revision, ProgressReport


class StudySessionAdmin(admin.ModelAdmin):
    list_display=('syllabus','topic','subtopic','duration_min','is_completed','created_at')


class RevisionAdmin(admin.ModelAdmin):
    list_display=('syllabus','subject','topic','date','revision_type')


class ProgressReportAdmin(admin.ModelAdmin):
    list_display=('syllabus','study_sessions','revisions','subjects','total_study_time_in_hours','total_revision_time_in_hours','created_at')
    

admin.site.register(StudySession,StudySessionAdmin)
admin.site.register(Revision,RevisionAdmin)
admin.site.register(ProgressReport,ProgressReportAdmin)