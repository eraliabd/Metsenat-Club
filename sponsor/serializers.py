from rest_framework import serializers

from .models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = [
            'id', 'full_name', 'phone', 'amount', 'used_amount', 'status', 'person_type', 'company_name', 'created_at'
        ]


# For none auth users
class SponsorAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'full_name', 'phone', 'amount', 'person_type', 'company_name', 'created_at']
