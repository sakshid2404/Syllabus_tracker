
from django.db import models
from accounts.models import User

class Syllabus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
<<<<<<< HEAD
=======
=======
        return self.name
<<<<<<< HEAD
=======
>>>>>>> 6a2beae6b079b7ab8e26ec8bcd9888130852c84b
>>>>>>> 5c90ba54847eff0b933159f165cdc1c1e6a698f2
>>>>>>> 230f2e019ee2793dd150dfa0840030729ed733a1
>>>>>>> 8af6a26cbf2de4c6ce15d3d58b51d664a35a4f88
