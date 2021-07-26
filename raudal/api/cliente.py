from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import ClienteSerializer
from raudal.models import Cliente


class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
