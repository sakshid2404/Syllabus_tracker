
from django.db import models


class Syllabus(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
       
       
       
    
    class Meta:
        verbose_name ="syllabus"
        verbose_name_plural = "syllabus"