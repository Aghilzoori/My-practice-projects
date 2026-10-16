from django.db import models

class Candidates(models.Model):
    fullname = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


# Create your models here.
