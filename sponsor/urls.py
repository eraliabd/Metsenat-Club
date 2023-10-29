from django.urls import path

from .views import SponsorAppListCreateAPIView, SponsorAppDetailAPIView, SponsorListCreateAPIView, SponsorDetailAPIView

urlpatterns = [
    path('sponsorapp/', SponsorAppListCreateAPIView.as_view(), name='sponsorapp'),
    path('sponsorapp/<int:pk>/', SponsorAppDetailAPIView.as_view(), name='sponsorapp-detail'),

    path('sponsor/', SponsorListCreateAPIView.as_view(), name='sponsor'),
    path('sponsor/<int:pk>/', SponsorDetailAPIView.as_view(), name='sponsor-detail'),
]
