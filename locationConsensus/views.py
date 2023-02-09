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

    context = {
        'num_interactions': num_interactions,
        'num_users': num_users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#######################################################################################

def verify(request, userID = ''):
    
    if User.objects.filter(userID=userID):
        output = userID + ' is in the database'
    else:
        output = userID + ' is NOT in the database'


    if userID == 'alex':
        output = 'lol XD alex is super smart'

    context = {
        'username': userID,
        'output': output
    }
    return render(request, 'verify.html', context=context)


#######################################################################################
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interactions to be viewed or edited.
    """
    queryset = Interaction.objects.all().order_by('-time')
    serializer_class = InteractionSerializer

class BlackistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows list of blacklisted users to be viewed or edited.
    """
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer