from django.db import models
from accounts.models import User
from subject.models import Topic, Subtopic, Subject,Chapter


class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    duration_min = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

   
class Revision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    revision_type = models.CharField(max_length=50, choices=[
        ("quick", "Quick Review"),
        ("detailed", "Detailed Review"),
        ("test", "Practice Test")
    ])
    
    def __str__(self):
     return f"Revision by {self.user.username} on {self.topic.title}"


class ProgressReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    study_sessions = models.ForeignKey(StudySession, on_delete=models.CASCADE)
    revisions = models.ForeignKey(Revision, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_study_time = models.PositiveIntegerField(help_text="Total study time in minutes", default=0)
    total_revision_time = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress Report - {self.user.username}"
