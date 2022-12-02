from rest_framework import serializers
from .models import Interaction, EphID, Location

class InteractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interaction
        fields = ['interactionID', 'spotter', 'spotted', 'location', 'time']

class EphIDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EphID
        fields = ['ephID']

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['location']