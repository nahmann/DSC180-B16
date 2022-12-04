from django.urls import include, path
from rest_framework import routers
from locationConsensus import views

router = routers.DefaultRouter()
router.register(r'interactions', views.InteractionViewSet, basename='interaction')
router.register(r'ephIDs', views.EphIDViewSet, basename='ephID')
router.register(r'locations', views.LocationViewSet, basename='location')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]