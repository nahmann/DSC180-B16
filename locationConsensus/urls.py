from django.urls import include, path
from rest_framework import routers
from locationConsensus import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'interactions', views.InteractionViewSet, basename='interaction')
router.register(r'blacklist', views.BlacklistViewSet, basename='blacklist')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('locationConsensus/', include((router.urls, 'locationConsensus'), namespace='locationConsensus')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns +=  staticfiles_urlpatterns()