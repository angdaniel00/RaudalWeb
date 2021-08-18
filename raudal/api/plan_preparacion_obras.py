from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import PlanPreparacionObrasSerializer
from ..models import PlanPreparacionObras


class PlanPreparacionObrasViewSet(ModelViewSet):
    serializer_class = PlanPreparacionObrasSerializer
    permission_classes = [IsAuthenticated]
    queryset = PlanPreparacionObras.objects.all()
