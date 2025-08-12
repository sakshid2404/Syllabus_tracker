
from django.db import models
from accounts.models import User

class Syllabus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.name 
>>>>>>> 3f69c6e6ab012e2ccaffc512e1d57db024f3651d
