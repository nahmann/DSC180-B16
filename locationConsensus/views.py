from rest_framework import viewsets
from django.shortcuts import render
from .models import *
from .serializers import *

#######################################################################################

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_interactions = Interaction.objects.count()
    num_users = Interaction.objects.all().distinct().count()

    context = {
        'num_interactions': num_interactions,
        'num_users': num_users,
        'num_blacklist': num_users,
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

class BlacklistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows list of blacklisted users to be viewed or edited.
    """
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer