from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to="static/images/")
    summary = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    edited = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title