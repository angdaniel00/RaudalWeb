from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND
from raudal.serializers import SuplContSerializer
from raudal.models import SuplementoContrato
from raudal.util.util import get_supl_cont_serializer


class SuplContViewSet(ModelViewSet):
    serializer_class = SuplContSerializer
    permission_classes = [IsAuthenticated]
    queryset = SuplementoContrato.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            supl_cont = SuplementoContrato.objects.get(year=kwargs['pk'])
            return Response(data=get_supl_cont_serializer(supl_cont.contrato_set.iterator()))
        except:
            return Response(status=HTTP_404_NOT_FOUND)
