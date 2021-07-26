from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import EntidadInversionistaSerializer
from raudal.models import EntidadInversionista


class EntidadInversionistaViewSet(ModelViewSet):
    serializer_class = EntidadInversionistaSerializer
    permission_classes = [IsAuthenticated]
    queryset = EntidadInversionista.objects.all()
