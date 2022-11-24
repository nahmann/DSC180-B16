from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# represents a location that has events happen at it
class Location(models.Model):
    location_text = models.CharField(max_length=200)

    def __str__(self):
        return self.location_text


# represents an ephID
class EphID(models.Model):
    ephID_text = models.CharField(max_length=200)

    def __str__(self):
        return self.ephID_text


# represents an interaction of 2 ephIDs at a location
class Interaction(models.Model):
    ephIDspotter = models.ForeignKey(EphID, on_delete=models.CASCADE) # ephID sending this interaction
    ephIDspotted = models.ForeignKey(EphID, on_delete=models.CASCADE) # ephID they claim to have spotted

    ephIDspotted = models.ForeignKey(Location, on_delete=models.CASCADE) # location of interaction
    
    
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)