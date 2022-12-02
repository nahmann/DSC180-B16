from rest_framework import viewsets
from .serializers import *
from .models import Interaction, EphID, Location

class InteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows interactions to be viewed or edited.
    """
    queryset = Interaction.objects.all().order_by('-time')
    serializer_class = InteractionSerializer

class EphIDViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows ephIDs to be viewed or edited.
    """
    queryset = EphID.objects.all().order_by('-ephID')
    serializer_class = EphIDSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows locations to be viewed or edited.
    """
    queryset = Location.objects.all().order_by('-location')
    serializer_class = LocationSerializer