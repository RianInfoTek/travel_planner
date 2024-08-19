# # itinerary/urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import   CrewAPIView

# router = DefaultRouter()
# # router.register(r'itinerary', ItineraryViewSet, basename='itinerary')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('crew/', CrewAPIView.as_view(), name='crew_api'),  # Add this line for the Crew API

# ]
# itinerary/urls.py

from django.urls import path
from .views import CrewAPIView

urlpatterns = [
    path('', CrewAPIView.as_view(), name='generate_itinerary'),  # This is the Crew API endpoint
]