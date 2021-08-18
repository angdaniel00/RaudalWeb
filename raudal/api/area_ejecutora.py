from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import AreaEjecutoraSerializer
from ..models import AreaEjecutora


class AreaEjecutoraViewSet(ModelViewSet):
    serializer_class = AreaEjecutoraSerializer
    permission_classes = [IsAuthenticated]
    queryset = AreaEjecutora.objects.all()
