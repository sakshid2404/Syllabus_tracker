from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Syllabus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

  
class Subject(models.Model):
    name = models.CharField(max_length=255)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    goal_hour = models.PositiveIntegerField()

    def __str__(self):
        return self.name

  
class Chapter(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=255)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subtopic(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title
    
   
class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
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