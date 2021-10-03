from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Document(models.Model):
    title = models.CharField(max_length = 64)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.CharField(max_length = 10 ** 7)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "owner": self.owner.email,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }

class Viewer(models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    Document = models.ForeignKey(Document, on_delete = models.CASCADE)
    canEdit = models.BooleanField(default = False)