from django.db import models
from login.models import *

# Create your models here.
class Discussion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length = 500)

    def __str__(self):
        return self.title

class DiscussionComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.CharField(max_length=500)

