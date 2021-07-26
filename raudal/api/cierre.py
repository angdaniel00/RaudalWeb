from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import CierreSerializer
from raudal.models import Cierre


class CierreViewSet(ModelViewSet):
    serializer_class = CierreSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cierre.objects.all()
