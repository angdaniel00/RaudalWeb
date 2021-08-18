from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import CierreSerializer
from ..models import Cierre


class CierreViewSet(ModelViewSet):
    serializer_class = CierreSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cierre.objects.all()
