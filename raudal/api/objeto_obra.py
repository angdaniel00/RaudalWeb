from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ObjetoObraSerializer
from ..models import ObjetoObra


class ObjetoObraViewSet(ModelViewSet):
    serializer_class = ObjetoObraSerializer
    permission_classes = [IsAuthenticated]
    queryset = ObjetoObra.objects.all()
