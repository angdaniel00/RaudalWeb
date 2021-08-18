from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ResumenContratacionSerializer
from ..models import ResumenContratacion


class ResumenContratacionViewSet(ModelViewSet):
    serializer_class = ResumenContratacionSerializer
    permission_classes = [IsAuthenticated]
    queryset = ResumenContratacion.objects.all()
