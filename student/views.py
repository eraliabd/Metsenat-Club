from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import University, Student, StudentSponsor, SponsorTransactions
from .serializers import UniversitySerializer, StudentSerializer, StudentSponsorSerializer, \
    SponsorTransactionsSerializer


class UniversityListCreateAPIView(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['study_type', 'university']


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentSponsorListCreateAPIView(ListCreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
