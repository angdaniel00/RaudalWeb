from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import ContratoSerializer
from ..models import Contrato


class ContratoViewSet(ModelViewSet):
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Contrato.objects.all()
