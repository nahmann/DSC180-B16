from rest_framework import viewsets
from .serializers import *
from django.shortcuts import render
from .models import Interaction

#######################################################################################

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_interactions = Interaction.objects.count()
    num_spotter = Interaction.objects.values('spotter').distinct().count()
    num_spotted = Interaction.objects.values('spotted').distinct().count()
    num_locations = Interaction.objects.values('location').distinct().count()

    context = {
        'num_interactions': num_interactions,
        'num_spotter': num_spotter,
        'num_spotted': num_spotted,
        'num_locations': num_locations,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


#######################################################################################

class InteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interactions to be viewed or edited.
    """
    queryset = Interaction.objects.all().order_by('-time')
    serializer_class = InteractionSerializer
