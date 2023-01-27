from rest_framework import viewsets
from django.shortcuts import render
from .models import *
from .serializers import *

#######################################################################################

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_interactions = Interaction.objects.count()
    num_users = User.objects.count()
    num_locations = Location.objects.count()

    context = {
        'num_interactions': num_interactions,
        'num_users': num_users,
        'num_locations': num_locations,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


#######################################################################################
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interactions to be viewed or edited.
    """
    queryset = Interaction.objects.all().order_by('-time')
    serializer_class = InteractionSerializer
