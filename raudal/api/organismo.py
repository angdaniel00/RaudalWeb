from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import OrganismoSerializer
from raudal.models import Organismo


class OrganismoViewSet(ModelViewSet):
    serializer_class = OrganismoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Organismo.objects.all()
