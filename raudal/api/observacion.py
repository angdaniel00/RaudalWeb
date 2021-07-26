from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import ObservacionSerializer
from raudal.models import Observacion


class ObservacionViewSet(ModelViewSet):
    serializer_class = ObservacionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Observacion.objects.all()
