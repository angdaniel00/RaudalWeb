from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import SuplememntoSerializer
from raudal.models import Suplemento


class SuplementoViewSet(ModelViewSet):
    serializer_class = SuplememntoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Suplemento.objects.all()
