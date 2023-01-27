from django.db import models
from django.utils import timezone

class User(models.Model):
    userID = models.CharField(max_length=20, primary_key=True, unique=True)

class Location(models.Model):
    locationID = models.CharField(max_length=20, primary_key=True, unique=True)

class Interaction(models.Model):
    interactionID = models.CharField(max_length=20)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spotter')
    spotted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spotted')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
