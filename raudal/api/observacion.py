from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ObservacionSerializer
from ..models import Observacion


class ObservacionViewSet(ModelViewSet):
    serializer_class = ObservacionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Observacion.objects.all()
