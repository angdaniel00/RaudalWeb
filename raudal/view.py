from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from .models import RegistroContabilidad, InformeGEIPI, Contrato, PlanPreparacionObras, Subcontrata, InformeProduccion, \
    InformeContratacion, SuplementoContrato
from .util.util import get_registro_contabilidad_serializer, get_informe_geipi_serializer, get_resumen_geipi_serializer, \
    get_serializer_informe_contratacion, get_supl_cont_serializer
from .util.util2 import get_serializer_inf_plan_prep_obras, get_serializer_subcontrata, get_serializer_inf_produccion


class InformeContratacionView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            inf = InformeContratacion.objects.get(year=kwargs['year'])
            return Response(data=get_serializer_informe_contratacion(inf.contrato_set.iterator()))
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class SuplContView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            supl_cont = SuplementoContrato.objects.get(year=kwargs['year'])
            return Response(data=get_supl_cont_serializer(supl_cont.contrato_set.iterator()))
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class RegistroContabilidadView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
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


# Duda
class ResumenContratacionView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            return Response()
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class ResumenGEIPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            year = kwargs['year']
            contratos = Contrato.objects.filter(resumen_geipi__year=year)
            return Response(data=get_resumen_geipi_serializer(contratos))
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class InfPlanPrepObrasView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            year = kwargs['year']
            plan = PlanPreparacionObras.objects.get(year=year)
            return Response(data=get_serializer_inf_plan_prep_obras(plan.contrato_set.iterator(), year))
        except:
            return Response(status=HTTP_404_NOT_FOUND)


# Duda
class SubContratasView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            month = kwargs['mes']
            year = kwargs['year']
            prov = kwargs['prov']
            subcontrata = Subcontrata.objects.get(year=year, mes=month)
            return Response(data=get_serializer_subcontrata(subcontrata, prov))
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class ProduccionView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            year = kwargs['year']
            return Response(data=get_serializer_inf_produccion(InformeProduccion.objects.get(year=year), year))
        except:
            return Response(status=HTTP_404_NOT_FOUND)
