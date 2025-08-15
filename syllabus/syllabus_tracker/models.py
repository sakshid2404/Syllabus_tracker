from django.db import models
from subject.models import Topic, Subtopic, Subject,Chapter
from accounts.models import User


class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    date = models.DateField()
    duration_min = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)
    

   
class Revision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    date = models.DateField()
    revision_type = models.CharField(max_length=50, choices=[
        ("quick", "Quick Review"),
        ("detailed", "Detailed Review"),
        ("test", "Practice Test")
    ])
    
    def __str__(self):
     return f"{self.topic.title}"


class ProgressReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    study_sessions = models.ForeignKey(StudySession, on_delete=models.CASCADE)
    revisions = models.ForeignKey(Revision, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)

    total_study_time_in_hours = models.FloatField(help_text="Total study time in hours", default=0.0)
    total_revision_time_in_hours = models.FloatField(help_text="Total revision time in hours", default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)


   
