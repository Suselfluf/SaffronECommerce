from rest_framework import serializers
from .models import SafrApp

class SaffrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafrApp
        fields = "__all__"