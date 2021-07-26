from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import InformeGEIPISerializer
from raudal.models import InformeGEIPI


class InformeGEIPIViewSet(ModelViewSet):
    serializer_class = InformeGEIPISerializer
    permission_classes = [IsAuthenticated]
    queryset = InformeGEIPI.objects.all()
