from django.db import models
from django.utils import timezone
import json

class User(models.Model):
    userID = models.CharField(max_length=20, primary_key=True, unique=True)
    verificationStatus = models.CharField(max_length=20, default='default')

class Interaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spotter')
    spotted_users = models.CharField(max_length=20)
    time = models.DateTimeField(default=timezone.now)

    def set_spotted_users (self, lst):
        self.spotted_users = json.dumps(lst)

    def get_spotted_users (self):
        return json.loads(self.spotted_users)