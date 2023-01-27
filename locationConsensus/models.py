from django.db import models
from django.utils import timezone

class User(models.Model):
    userID = models.CharField(max_length=20, primary_key=True, unique=True)

    def __str__(self):
        return self.userID

class Location(models.Model):
    locationID = models.CharField(max_length=20, primary_key=True, unique=True)

    def __str__(self):
        return self.locationID

class Interaction(models.Model):
    interactionID = models.CharField(max_length=20)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    spotted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.interactionID