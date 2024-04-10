from django.db import models
from django.utils import timezone

class Message(models.Model):
    message = models.TextField()
    user_id = models.TextField()
    channel = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)