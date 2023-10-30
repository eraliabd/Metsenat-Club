from django.urls import path

from .views import SponsorListAPIView, SponsorCreateAPIView, SponsorDetailAPIView

urlpatterns = [
    path('sponsor/', SponsorListAPIView.as_view(), name='sponsor-list'),
    path('sponsor/create/', SponsorCreateAPIView.as_view(), name='sponsor-create'),
    path('sponsor/<int:pk>/', SponsorDetailAPIView.as_view(), name='sponsor-detail'),
]
