from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import ContratoSerializer
from raudal.models import Contrato


class ContratoViewSet(ModelViewSet):
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Contrato.objects.all()
