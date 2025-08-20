from django.db import models
from subject.models import Topic, Subtopic, Subject,Chapter,Syllabus



class StudySession(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    duration_min = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.subject.name} - {self.topic.title} ({self.duration_min} mins)"

   
class Revision(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
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
         return f"{self.subject} - {self.revision_type} on {self.date}"



class ProgressReport(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE) 
    study_sessions = models.ForeignKey(StudySession, on_delete=models.CASCADE)
    revisions = models.ForeignKey(Revision, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)

    total_study_time_in_hours = models.IntegerField(help_text="Total study time in hours")
    total_revision_time_in_hours = models.IntegerField(help_text="Total revision time in hours")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"Progress Report for {self.syllabus} - {self.created_at.date()}"


   
