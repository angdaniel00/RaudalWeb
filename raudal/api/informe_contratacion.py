from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import InformeContratacionSerializer
from ..models import InformeContratacion


class InformeContratacionViewSet(ModelViewSet):
    serializer_class = InformeContratacionSerializer
    permission_classes = [IsAuthenticated]
    queryset = InformeContratacion.objects.all()
