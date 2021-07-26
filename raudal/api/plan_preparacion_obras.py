from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from raudal.serializers import PlanPreparacionObrasSerializer
from raudal.models import PlanPreparacionObras


class PlanPreparacionObrasViewSet(ModelViewSet):
    serializer_class = PlanPreparacionObrasSerializer
    permission_classes = [IsAuthenticated]
    queryset = PlanPreparacionObras.objects.all()
