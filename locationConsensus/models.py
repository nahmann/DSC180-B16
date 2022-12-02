from django.db import models
from django.utils import timezone
import datetime

class EphID(models.Model):
    ephID = models.CharField(max_length=200)

    def __str__(self):
        return self.ephID

class Location(models.model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location

class Interaction(models.Model):
    interactionID = models.CharField(max_length=200)

    spotter = models.ForeignKey(EphID, on_delete=models.CASCADE)
    spotted = models.ForeignKey(EphID, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time = models.DateTimeField('time occured')

    def __str__(self):
        return self.interactionID

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)