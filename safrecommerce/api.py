from .models import *
from rest_framework import viewsets, permissions
from .serializers import SaffrSerializer


class SaffrViewSet(viewsets.ModelViewSet):
    queryset = SaffronProducts.objects.all(), SaffroonBGInfo.objects.all(), CommercialOfferParameeters.objects.all(), ContactInfo.objects.all(), CustomerOfferModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SaffrSerializer