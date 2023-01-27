from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userID']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['locationID']

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['interactionID', 'from_user', 'spotted_user', 'location', 'time']