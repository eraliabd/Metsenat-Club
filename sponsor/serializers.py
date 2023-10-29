from rest_framework import serializers

from .models import Sponsor, SponsorApplication


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = ['id', 'full_name', 'phone', 'amount', 'used_amount', 'status']


class NoneSponsorApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorApplication
        fields = ['id', 'full_name', 'phone', 'amount', 'type', 'company_name']


class SponsorApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorApplication
        fields = ['id', 'full_name', 'phone', 'amount', 'type', 'company_name']
