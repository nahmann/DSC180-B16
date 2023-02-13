from django.db import models
from django.utils import timezone
import json

class User(models.Model):
    userID = models.CharField(max_length=20, primary_key=True, unique=True)

class Interaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    spotted_users = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

class Blacklist(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')