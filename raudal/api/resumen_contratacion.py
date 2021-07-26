from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import ResumenContratacionSerializer
from raudal.models import ResumenContratacion


class ResumenContratacionViewSet(ModelViewSet):
    serializer_class = ResumenContratacionSerializer
    permission_classes = [IsAuthenticated]
    queryset = ResumenContratacion.objects.all()
