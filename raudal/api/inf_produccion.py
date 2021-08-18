from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..serializers import InfProduccionSerializer
from ..models import InformeProduccion


class InformeProduccionViewSet(ModelViewSet):
    serializer_class = InfProduccionSerializer
    permission_classes = [IsAuthenticated]
    queryset = InformeProduccion.objects.all()
