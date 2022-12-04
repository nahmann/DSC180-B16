from django.db import models
from django.utils import timezone
import datetime

class EphID(models.Model):
    ephID = models.CharField(max_length=20)

    def __str__(self):
        return self.ephID

class Location(models.Model):
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.location

class Interaction(models.Model):
    interactionID = models.CharField(max_length=20)
    spotter = models.ForeignKey(EphID, on_delete=models.CASCADE, related_name='EphID_spotters')
    spotted = models.ForeignKey(EphID, on_delete=models.CASCADE, related_name='EphIDs_spotted')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locations')
    time = models.DateTimeField('time occured')

    def __str__(self):
        return self.interactionID

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)