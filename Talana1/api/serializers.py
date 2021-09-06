from .models import ClUserData
from rest_framework import serializers


class ClUserDataSerializer(serializers.ModelSerializer):
    rut = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return ClUserData.objects.create(**validated_data)
