from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import OrganismoSerializer
from ..models import Organismo


class OrganismoViewSet(ModelViewSet):
    serializer_class = OrganismoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Organismo.objects.all()
