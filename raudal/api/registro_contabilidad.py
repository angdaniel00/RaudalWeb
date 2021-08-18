from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import RegistroContabilidadSerializer
from ..models import RegistroContabilidad


class RegistroContabilidadViewSet(ModelViewSet):
    serializer_class = RegistroContabilidadSerializer
    permission_classes = [IsAuthenticated]
    queryset = RegistroContabilidad.objects.all()
