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