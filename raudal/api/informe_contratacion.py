from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND
from raudal.serializers import InformeContratacionSerializer
from raudal.models import InformeContratacion
from raudal.util.util import get_serializer_informe_contratacion


class InformeContratacionViewSet(ModelViewSet):
    serializer_class = InformeContratacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InformeContratacion.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            inf = InformeContratacion.objects.get(year=kwargs['pk'])
            return Response(data=get_serializer_informe_contratacion(inf.contrato_set.iterator()))
        except:
            return Response(status=HTTP_404_NOT_FOUND)
