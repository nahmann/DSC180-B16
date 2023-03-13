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

def runScript(request):
    num_blacklist_before = Blacklist.objects.count()

    if request.method == 'POST' and 'run_script' in request.POST:
        import run_algorithm

    num_blacklist_after = Blacklist.objects.count()
    num_interactions = Interaction.objects.count()
    context = {
        'num_blacklist_after' : num_blacklist_after,
        'num_blacklist_before' : num_blacklist_before,
        'num_interactions' : num_interactions,
    }
    return render(request, 'runScript.html', context=context)

#######################################################################################

def clearBlacklist(request):
    num_before = Blacklist.objects.count()
    Blacklist.objects.all().delete()
    num_after = Blacklist.objects.count()

    context = {
        'type' : 'blacklist',
        'num_before' : num_before,
        'num_after' : num_after,
    }

    return render(request, 'clear_success.html', context=context)

def clearInteractions(request):
    num_before = Interaction.objects.count()
    Interaction.objects.all().delete()
    num_after = Interaction.objects.count()

    context = {
        'type' : 'interactions',
        'num_before' : num_before,
        'num_after' : num_after,
    }

    return render(request, 'clear_success.html', context=context)

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