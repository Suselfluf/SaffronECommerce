from .models import SafrApp
from rest_framework import viewsets, permissions
from .serializers import SaffrSerializer


class SaffrViewSet(viewsets.ModelViewSet):
    queryset = SafrApp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SaffrSerializer