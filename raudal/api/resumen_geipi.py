from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ResumenGEIPISerializer
from ..models import ResumenGEIPI


class ResumenGEIPIViewSet(ModelViewSet):
    serializer_class = ResumenGEIPISerializer
    permission_classes = [IsAuthenticated]
    queryset = ResumenGEIPI.objects.all()
