from rest_framework import routers
from django.urls import path
from raudal.api.cierre import CierreViewSet
from raudal.api.cliente import ClienteViewSet
from raudal.api.contrato import ContratoViewSet
from raudal.api.area_ejecutora import AreaEjecutoraViewSet
from raudal.api.entidad_inversionista import EntidadInversionistaViewSet
from raudal.api.informe_contratacion import InformeContratacionViewSet
from raudal.api.informe_geipi import InformeGEIPIViewSet
from raudal.api.objeto_obra import ObjetoObraViewSet
from raudal.api.observacion import ObservacionViewSet
from raudal.api.organismo import OrganismoViewSet
from raudal.api.plan_preparacion_obras import PlanPreparacionObrasViewSet
from raudal.api.registro_contabilidad import RegistroContabilidadViewSet
from raudal.api.resumen_contratacion import ResumenContratacionViewSet
from raudal.api.resumen_geipi import ResumenGEIPIViewSet
from raudal.api.subcontrata import SubContrataViewSet
from raudal.api.supl_cont import SuplContViewSet
from raudal.api.suplemento import SuplementoViewSet
from .view import RegistroContabilidadView, InformeGEIPIView


router = routers.DefaultRouter()
router.register(r'cierre', CierreViewSet, basename='cierre')
router.register(r'cliente', ClienteViewSet, basename='cliente')
router.register(r'contrato', ContratoViewSet, basename='contrato')
router.register(r'area', AreaEjecutoraViewSet, basename='area_ejecutora')
router.register(r'inversionista', EntidadInversionistaViewSet, basename='entidad_inversionista')
router.register(r'infcontratacion', InformeContratacionViewSet, basename='informe_contratacion')
router.register(r'infgeipi', InformeGEIPIViewSet, basename='informe_geipi')
router.register(r'objobra', ObjetoObraViewSet, basename='objeto_obra')
router.register(r'observacion', ObservacionViewSet, basename='observacion')
router.register(r'organismo', OrganismoViewSet, basename='organismo')
router.register(r'planobras', PlanPreparacionObrasViewSet, basename='plan_obras')
router.register(r'regcontabilidad', RegistroContabilidadViewSet, basename='registro_contabilidad')
router.register(r'resumen/contratacion', ResumenContratacionViewSet, basename='registro_contratacion')
router.register(r'resumen/geipi', ResumenGEIPIViewSet, basename='resumen_geipi')
router.register(r'subcontrata', SubContrataViewSet, basename='subcontrata')
router.register(r'suplemento', SuplementoViewSet, basename='suplemento')
router.register(r'suplcont', SuplContViewSet, basename='suplemento_contrato')

urlpatterns = [
    path('registro_contabilidad/<str:mes>/<str:area>/', RegistroContabilidadView.as_view(), name='view_registro'),
    path('informegeipi/<str:plan>/<str:area>/', InformeGEIPIView.as_view(), name='view_informe_geipi')
]

urlpatterns += router.urls
