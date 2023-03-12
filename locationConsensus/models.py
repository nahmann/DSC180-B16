from django.db import models
from django.utils import timezone
import json

class Interaction(models.Model):
    from_user = models.CharField(max_length=32)
    spotted_users = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

class Blacklist(models.Model):
    userID = models.CharField(max_length=32)