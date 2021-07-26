from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from raudal.models import RegistroContabilidad, InformeGEIPI
from raudal.util.util import get_registro_contabilidad_serializer, get_informe_geipi_serializer


class RegistroContabilidadView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request: Request, *args, **kwargs):
        try:
            reg = RegistroContabilidad.objects.get(mes=kwargs['mes'])
            return Response(data=get_registro_contabilidad_serializer(reg.contrato_set.iterator(), kwargs['area']))
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class InformeGEIPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            inf = InformeGEIPI.objects.get(plan_anual=kwargs['plan'])
            return Response(data=get_informe_geipi_serializer(inf.contrato_set.iterator(), kwargs['area']))
        except:
            return Response(status=HTTP_404_NOT_FOUND)
