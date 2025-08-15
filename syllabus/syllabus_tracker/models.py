from django.db import models
from subject.models import Topic, Subtopic, Subject,Chapter


class StudySession(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    date = models.DateField()
    duration_min = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return str(self.date)
=======
        return f"{self.date}"
>>>>>>> 3d75138126cb3fff9bad839173cb6795ce19e372

   
class Revision(models.Model):
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
    date = models.DateField()
    study_sessions = models.ForeignKey(StudySession, on_delete=models.CASCADE)
    revisions = models.ForeignKey(Revision, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_study_time = models.PositiveIntegerField(help_text="Total study time in minutes", default=0)
    total_revision_time = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD
   
=======
>>>>>>> 3d75138126cb3fff9bad839173cb6795ce19e372
