from rest_framework import serializers

from .models import Student, StudentSponsor, University, SponsorTransactions


class UniversitySerializers(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ['id', 'title']


class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'university', 'study_type', 'required_amount', 'payed_amount']


class StudentSponsorSerializers(serializers.ModelSerializer):

    class Meta:
        model = StudentSponsor
        fields = ['id', 'full_name', 'university', 'study_type', 'required_amount', 'payed_amount']


class SponsorTransactionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = SponsorTransactions
        fields = ['id', 'student', 'sponsor', 'amount', 'is_success']
