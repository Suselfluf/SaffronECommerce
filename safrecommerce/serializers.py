from rest_framework import serializers
from .models import *

class SaffrSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaffronProducts, SaffroonBGInfo, CommercialOfferParameeters, ContactInfo
        fields = "__all__"