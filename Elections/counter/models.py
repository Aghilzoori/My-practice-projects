from django.db import models
from manager.models import Candidates


class Vote(models.Model):
    fullname = models.CharField(max_length=400)
    national_code = models.CharField(max_length=100)
    candidate_id = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


# Create your models here.
