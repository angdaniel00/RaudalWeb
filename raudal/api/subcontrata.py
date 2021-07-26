from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import SubContrataSerializer
from raudal.models import Subcontrata


class SubContrataViewSet(ModelViewSet):
    serializer_class = SubContrataSerializer
    permission_classes = [IsAuthenticated]
    queryset = Subcontrata.objects.all()
