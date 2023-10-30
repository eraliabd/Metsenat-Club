from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import University, Student, StudentSponsor, SponsorTransactions
from .serializers import UniversitySerializer, StudentSerializer, StudentSponsorSerializer, \
    SponsorTransactionsSerializer


class UniversityAPIView(ModelViewSet):
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


class SponsorTransactionsListCreateAPIView(ListCreateAPIView):
    queryset = SponsorTransactions.objects.all()
    serializer_class = SponsorTransactionsSerializer

    def create(self, request, *args, **kwargs):
        serializer = SponsorTransactionsSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        # trans = SponsorTransactions.objects.create(
        #     student=request.data['student'],
        #     sponsor=request.data['sponsor'],
        #     amount=request.data['amount'],
        #     is_success=request.data['is_success'],
        # )
        trans = serializer.data
        result = SponsorTransactionsSerializer(trans)
        return Response(result.data, status=status.HTTP_201_CREATED)


