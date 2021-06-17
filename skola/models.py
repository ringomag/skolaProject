from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title