from django.urls import path

from .views import SponsorListAPIView, SponsorCreateAPIView, SponsorDetailAPIView, TotalAmountPaidBySponsor

urlpatterns = [
    path('', SponsorListAPIView.as_view(), name='sponsor-list'),
    path('create/', SponsorCreateAPIView.as_view(), name='sponsor-create'),
    path('<int:pk>/', SponsorDetailAPIView.as_view(), name='sponsor-detail'),
    path('total-amount/', TotalAmountPaidBySponsor.as_view(), name='sponsor-total-amount'),
]
