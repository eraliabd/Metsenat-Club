from rest_framework import serializers

from .models import Student, StudentSponsor, University, SponsorTransactions


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ['id', 'title']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'phone', 'university', 'study_type', 'required_amount', 'payed_amount']


class StudentSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSponsor
        fields = ['id', 'sponsor', 'student', 'amount', 'created_at']


class SponsorTransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorTransactions
        fields = ['id', 'student', 'sponsor', 'amount', 'is_success', 'created_at']
