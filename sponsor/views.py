from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Sponsor, SponsorApplication
from .serializers import SponsorSerializer, SponsorApplicationSerializer


class SponsorAppListCreateAPIView(ListCreateAPIView):
    queryset = SponsorApplication.objects.all()
    serializer_class = SponsorApplicationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['amount', 'status', 'created_at']


class SponsorAppDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SponsorApplication.objects.all()
    serializer_class = SponsorApplicationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['amount', 'status', 'created_at']


class SponsorListCreateAPIView(ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
