from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    body = models.CharField(max_length=4000, blank=False)

    def __str__(self):
        return self.title
