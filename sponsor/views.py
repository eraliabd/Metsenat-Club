from django.db.models import Sum
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Sponsor
from .serializers import SponsorSerializer, SponsorAppSerializer


# For none auth user
class SponsorCreateAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorAppSerializer


class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.order_by('-created_at')
    serializer_class = SponsorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['amount', 'status', 'created_at']


class SponsorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class TotalAmountPaidBySponsor(ListAPIView):
    queryset = Sponsor.objects.all().annotate(total_sum=Sum('used_amount'))
    serializer_class = SponsorSerializer
