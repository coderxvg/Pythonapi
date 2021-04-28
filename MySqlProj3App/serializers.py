from rest_framework import serializers

from .models import CcrFormnew


class CcrFormSerializer(serializers.Serializer):
    Requestor = serializers.CharField(max_length=100)
    Role = serializers.CharField(max_length=100)
    
    def create(self, validate_data):
        return CcrFormnew.objects.create(**validate_data)