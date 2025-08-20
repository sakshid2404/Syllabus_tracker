from django.db import models
from app.models import Syllabus

  
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
    
