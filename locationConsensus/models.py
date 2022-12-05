from django.db import models

class Interaction(models.Model):
    interactionID = models.CharField(max_length=20)
    spotter = models.CharField(max_length=20)
    spotted = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    time = models.DateTimeField('time occured')

    def __str__(self):
        return self.interactionID