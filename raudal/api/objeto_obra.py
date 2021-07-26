from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import ObjetoObraSerializer
from raudal.models import ObjetoObra


class ObjetoObraViewSet(ModelViewSet):
    serializer_class = ObjetoObraSerializer
    permission_classes = [IsAuthenticated]
    queryset = ObjetoObra.objects.all()
