#######################################################################################

from django.shortcuts import render
from locationConsensus.models import *

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_interactions = Interaction.objects.count()
    num_ephIDs = EphID.objects.count()

    context = {
        'num_interactions': num_interactions,
        'num_ephIDs': num_ephIDs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


#######################################################################################

from rest_framework import viewsets, generics
from .serializers import *
from .models import Interaction, EphID, Location

class InteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interactions to be viewed or edited.
    """
    queryset = Interaction.objects.all().order_by('-time')
    serializer_class = InteractionSerializer

class EphIDViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ephIDs to be viewed or edited.
    """
    queryset = EphID.objects.all().order_by('-ephID')
    serializer_class = EphIDSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows locations to be viewed or edited.
    """
    queryset = Location.objects.all().order_by('-location')
    serializer_class = LocationSerializer
