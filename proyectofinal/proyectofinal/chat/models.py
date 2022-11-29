from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.sender} --> {self.receiver}'