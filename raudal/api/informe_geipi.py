from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import InformeGEIPISerializer
from ..models import InformeGEIPI


class InformeGEIPIViewSet(ModelViewSet):
    serializer_class = InformeGEIPISerializer
    permission_classes = [IsAuthenticated]
    queryset = InformeGEIPI.objects.all()
