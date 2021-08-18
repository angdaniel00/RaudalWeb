from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import SuplContSerializer
from ..models import SuplementoContrato


class SuplContViewSet(ModelViewSet):
    serializer_class = SuplContSerializer
    permission_classes = [IsAuthenticated]
    queryset = SuplementoContrato.objects.all()
