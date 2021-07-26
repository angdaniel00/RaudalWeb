from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import RegistroContabilidadSerializer
from raudal.models import RegistroContabilidad


class RegistroContabilidadViewSet(ModelViewSet):
    serializer_class = RegistroContabilidadSerializer
    permission_classes = [IsAuthenticated]
    queryset = RegistroContabilidad.objects.all()
