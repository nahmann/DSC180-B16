from django.shortcuts import render

# Create your views here.

from .models import Interaction

class IndexView(generic.ListView):
    template_name = 'test1/index.html'
    context_object_name = 'latest_interactions_list'

    def get_queryset(self):
        """Return the last five published interactions."""
        return Interaction.objects.order_by('-pub_date')[:5]

    