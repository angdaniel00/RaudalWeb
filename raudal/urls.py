from rest_framework import routers
from django.urls import path
from .api.cierre import CierreViewSet
from .api.cliente import ClienteViewSet
from .api.contrato import ContratoViewSet
from .api.area_ejecutora import AreaEjecutoraViewSet
from .api.entidad_inversionista import EntidadInversionistaViewSet
from .api.informe_contratacion import InformeContratacionViewSet
from .api.informe_geipi import InformeGEIPIViewSet
from .api.objeto_obra import ObjetoObraViewSet
from .api.observacion import ObservacionViewSet
from .api.organismo import OrganismoViewSet
from .api.plan_preparacion_obras import PlanPreparacionObrasViewSet
from .api.registro_contabilidad import RegistroContabilidadViewSet
from .api.resumen_contratacion import ResumenContratacionViewSet
from .api.resumen_geipi import ResumenGEIPIViewSet
from .api.subcontrata import SubContrataViewSet
from .api.supl_cont import SuplContViewSet
from .api.suplemento import SuplementoViewSet
from .api.inf_produccion import InformeProduccionViewSet
from .view import RegistroContabilidadView, InformeGEIPIView, ResumenGEIPIView, InfPlanPrepObrasView, SubContratasView, \
    ProduccionView, InformeContratacionView, SuplContView


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
router.register(r'infproduccion', InformeProduccionViewSet, basename='informe_produccion')

urlpatterns = [
    path('inf/contratacion/<int:year>/', InformeContratacionView.as_view(), name='view_inf_contratacion'),
    path('inf/suplcont/<int:year>/', SuplContView.as_view(), name='view_supl_cont'),
    path('registro_contabilidad/<str:mes>/<str:area>/', RegistroContabilidadView.as_view(), name='view_registro'),
    path('informegeipi/<str:plan>/<str:area>/', InformeGEIPIView.as_view(), name='view_informe_geipi'),
    path('resumengeipi/<int:year>/', ResumenGEIPIView.as_view(), name='view_resumen_geipi'),
    path('plan/<int:year>/', InfPlanPrepObrasView.as_view(), name='view_plan_obras'),
    path('inf/subcontrata/<int:year>/<int:mes>/<str:prov>/', SubContratasView.as_view(), name='view_subcontrata'),
    path('inf/produccion/<int:year>/', ProduccionView.as_view(), name='view_produccion')
]

urlpatterns += router.urls
