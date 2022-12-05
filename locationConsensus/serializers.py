from rest_framework import serializers
from .models import *

class InteractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interaction
        fields = ['interactionID', 'spotter', 'spotted', 'location', 'time']