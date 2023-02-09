from django.urls import include, path
from rest_framework import routers
from locationConsensus import views

router = routers.DefaultRouter()
router.register(r'interactions', views.InteractionViewSet, basename='interaction')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'blacklist', views.BlackistViewSet, basename='blacklist')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('locationConsensus/', include((router.urls, 'locationConsensus'), namespace='locationConsensus')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('verify/<userID>/', views.verify, name='verify')
]