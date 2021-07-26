from .models import *
from raudal.util.util import get_fields_serializer
from rest_framework.utils import model_meta
from rest_framework.serializers import ModelSerializer, IntegerField, ListField, FloatField


class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    def create(self, validated_data):
        client = Cliente.objects.create(name=validated_data['name'])
        return client

    def update(self, instance: Cliente, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance


class CierreSerializer(ModelSerializer):
    id_informe_contratacion = IntegerField(required=False)

    class Meta:
        model = Cierre
        fields = '__all__'

    def create(self, validated_data):
        cierre = Cierre.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'id_informe_contratacion' in validated_data and validated_data['id_informe_contratacion']:
            inf = InformeContratacion.objects.get(id__exact=validated_data['id_informe_contratacion'])
            inf.cierre = cierre
            inf.save()

        return cierre

    def update(self, instance: Cierre, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'id_informe_contratacion' in validated_data:
            inf = InformeContratacion.objects.get(id__exact=validated_data['id_informe_contratacion'])
            inf.cierre = instance
            inf.save()

        instance.save()
        return instance


class ResumenGEIPISerializer(ModelSerializer):
    list_informe_contratacion = ListField(required=False)

    class Meta:
        model = ResumenGEIPI
        fields = '__all__'

    def create(self, validated_data):
        resumen = ResumenGEIPI.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_informe_contratacion' in validated_data and len(validated_data['list_informe_contratacion']) > 0:
            list_informe_contratacion = InformeContratacion.objects.filter(id__in=validated_data['list_informe_contratacion'])
            resumen.informecontratacion_set.add(*list_informe_contratacion)
            resumen.save()

        return resumen

    def update(self, instance: ResumenGEIPI, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_informe_contratacion' in validated_data:
            list_inf = InformeContratacion.objects.filter(id__in=validated_data['list_informe_contratacion'])
            instance.informecontratacion_set.add(*list_inf)

        instance.save()
        return instance


class PlanPreparacionObrasSerializer(ModelSerializer):
    list_informe_contratacion = ListField(required=False)

    class Meta:
        model = PlanPreparacionObras
        fields = '__all__'

    def create(self, validated_data):
        plan = PlanPreparacionObras.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_informe_contratacion' in validated_data and len(validated_data['list_informe_contratacion']) > 0:
            list_informe_contratacion = InformeContratacion.objects.filter(id__in=validated_data['list_informe_contratacion'])
            plan.informecontratacion_set.add(*list_informe_contratacion)
            plan.save()

        return plan

    def update(self, instance: PlanPreparacionObras, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_informe_contratacion' in validated_data:
            list_informe_contratacion = InformeContratacion.objects.filter(id__in=validated_data['list_informe_contratacion'])
            instance.informecontratacion_set.add(*list_informe_contratacion)

        instance.save()
        return instance


class AreaEjecutoraSerializer(ModelSerializer):
    id_objeto_obras = IntegerField(required=False)
    id_contrato = IntegerField(required=False)

    class Meta:
        model = AreaEjecutora
        fields = '__all__'

    def create(self, validated_data):
        if 'id_objeto_obras' in validated_data and validated_data['id_objeto_obras']:
            obj = ObjetoObra.objects.get(id__exact=validated_data['id_objeto_obras'])
            validated_data['objeto_obra'] = obj

        if 'id_contrato' in validated_data and validated_data['id_contrato']:
            cont = Contrato.objects.get(id__exact=validated_data['id_contrato'])
            validated_data['contrato'] = cont

        area = AreaEjecutora.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        return area

    def update(self, instance: AreaEjecutora, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr == 'objeto_obra':
                if 'id_objeto_obras' not in validated_data or (instance.objeto_obra and validated_data['id_objeto_obras'] == instance.objeto_obra.id):
                    continue
                else:
                    value = ObjetoObra.objects.get(id__exact=validated_data['id_objeto_obras'])
            if attr == 'contrato':
                if 'id_contrato' not in validated_data or (instance.contrato and validated_data['id_contrato'] == instance.contrato.id):
                    continue
                else:
                    value = Contrato.objects.get(id__exact=validated_data['id_contrato'])
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance


class ObjetoObraSerializer(ModelSerializer):
    id_suplemento = IntegerField(required=False)
    list_observaciones = ListField(required=False)
    list_area_ejecutora = ListField(required=False)

    class Meta:
        model = ObjetoObra
        fields = '__all__'

    def create(self, validated_data):
        obj = ObjetoObra.objects.create(**get_fields_serializer(self.Meta.model, validated_data))
        change = False

        if 'id_suplemento' in validated_data and validated_data['id_suplemento']:
            supl = Suplemento.objects.get(id__exact=validated_data['id_suplemento'])
            supl.objeto = obj
            supl.save()

        if 'list_observaciones' in validated_data and len(validated_data['list_observaciones']) > 0:
            list_obs = Observacion.objects.filter(id__in=validated_data['list_observaciones'])
            obj.observacion_set.add(*list_obs)
            change = True

        if 'list_area_ejecutora' in validated_data and len(validated_data['list_area_ejecutora']) > 0:
            list_area = AreaEjecutora.objects.filter(id__in=validated_data['list_area_ejecutora'])
            obj.areaejecutora_set.add(*list_area)
            change = True

        if change is True:
            obj.save()

        return obj

    def update(self, instance: ObjetoObra, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_observaciones' in validated_data:
            list_observaciones = Observacion.objects.filter(id__in=validated_data['list_observaciones'])
            instance.observacion_set.add(*list_observaciones)

        if 'list_area_ejecutora' in validated_data:
            list_area_ejecutora = AreaEjecutora.objects.filter(id__in=validated_data['list_area_ejecutora'])
            instance.areaejecutora_set.add(*list_area_ejecutora)

        if 'id_suplemento' in validated_data and instance.suplemento.id != validated_data['id_suplemento']:
            supl = Suplemento.objects.get(id__exact=validated_data['id_suplemento'])
            supl.objeto = instance
            supl.save()

        instance.save()
        return instance


class ObservacionSerializer(ModelSerializer):
    id_objeto_obra = IntegerField(required=False)

    class Meta:
        model = Observacion
        fields = '__all__'

    def create(self, validated_data):
        if 'id_objeto_obra' in validated_data and validated_data['id_objeto_obra']:
            validated_data['objeto_obra'] = ObjetoObra.objects.get(id=validated_data['id_objeto_obra'])

        obs = Observacion.objects.create(**get_fields_serializer(self.Meta.model, validated_data))
        return obs

    def update(self, instance: Observacion, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr == 'objeto_obra':
                if instance.objeto_obra and validated_data['id_objeto_obra'] == instance.objeto_obra.id:
                    continue
                else:
                    value = ObjetoObra.objects.get(id__exact=validated_data['id_objeto_obra'])
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class RegistroContabilidadSerializer(ModelSerializer):
    list_contrato = ListField(required=False)

    class Meta:
        model = RegistroContabilidad
        fields = '__all__'

    def create(self, validated_data):
        reg = RegistroContabilidad.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and len(validated_data['list_contrato']) > 0:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            reg.contrato_set.add(*list_contrato)
            reg.save()

        return reg

    def update(self, instance: RegistroContabilidad, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data:
            list_cont = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_cont)

        instance.save()
        return instance


class InformeContratacionSerializer(ModelSerializer):
    list_contrato = ListField(required=False)
    id_plan_preparacion_obras = IntegerField(required=False)
    id_cierre = IntegerField(required=False)
    id_resumen_geipi = IntegerField(required=False)

    class Meta:
        model = InformeContratacion
        fields = '__all__'

    def create(self, validated_data):
        if 'id_plan_preparacion_obras' in validated_data:
            validated_data['plan'] = PlanPreparacionObras.objects.get(id__exact=validated_data['id_plan_preparacion_obras'])

        if 'id_cierre' in validated_data:
            validated_data['cierre'] = Cierre.objects.get(id__exact='id_cierre')

        if 'id_resumen_geipi' in validated_data:
            validated_data['resumenGEIPI'] = ResumenGEIPI.objects.get(id__exact=validated_data['id_resumen_geipi'])

        inf = InformeContratacion.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            inf.contrato_set.add(*list_contrato)
            inf.save()

        return inf

    def update(self, instance: InformeContratacion, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr == 'plan':
                if 'id_plan_preparacion_obras' not in validated_data or (instance.plan and validated_data['id_plan_preparacion_obras'] == instance.plan.id):
                    continue
                else:
                    value = PlanPreparacionObras.objects.get(id__exact=validated_data['id_plan_preparacion_obras'])
            if attr == 'cierre':
                if 'id_cierre' not in validated_data or (instance.cierre and validated_data['id_cierre'] == instance.cierre.id):
                    continue
                else:
                    value = Cierre.objects.get(id__exact=validated_data['id_cierre'])
            if attr == 'resumenGEIPI':
                if 'id_resumen_geipi' not in validated_data or (instance.resumenGEIPI and validated_data['id_resumen_geipi'] == instance.resumenGEIPI.id):
                    continue
                else:
                    value = ResumenGEIPI.objects.get(id__exact=validated_data['id_resumen_geipi'])
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data and validated_data['list_contrato']:
            list_contrato = Contrato.objects.filter(id__exact=validated_data['list_contrato'])
            instance.contrato_set.add(*list_contrato)

        instance.save()
        return instance


class InformeGEIPISerializer(ModelSerializer):
    list_contrato = ListField(required=False)

    class Meta:
        model = InformeGEIPI
        fields = '__all__'

    def create(self, validated_data):
        inf = InformeGEIPI.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and len(validated_data['list_contrato']) > 0:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            inf.contrato_set.add(*list_contrato)
            inf.save()

        return inf

    def update(self, instance: InformeGEIPI, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data and len(validated_data['list_contrato']) > 0:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_contrato)

        instance.save()
        return instance


class SuplememntoSerializer(ModelSerializer):
    id_contrato = IntegerField(required=False)
    id_objeto = IntegerField(required=False)
    valor_actual_contrato_inc_supl = FloatField(required=False)

    class Meta:
        model = Suplemento
        fields = '__all__'

    def create(self, validated_data):
        if 'id_contrato' in validated_data and validated_data['id_contrato']:
            validated_data['contrato'] = Contrato.objects.get(id__exact=validated_data['id_contrato'])

        if 'id_objeto' in validated_data and validated_data['id_objeto']:
            validated_data['objeto'] = ObjetoObra.objects.get(id__exact=validated_data['id_objeto'])

        supl = Suplemento.objects.create(**get_fields_serializer(self.Meta.model, validated_data))
        return supl

    def update(self, instance: Suplemento, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr == 'contrato':
                if 'id_contrato' not in validated_data or (instance.contrato and validated_data['id_contrato'] == instance.contrato.id):
                    continue
                else:
                    value = Contrato.objects.get(id__exact=validated_data['id_contrato'])
            if attr == 'objeto':
                if 'id_objeto' not in validated_data or (instance.objeto and validated_data['id_objeto'] == instance.objeto.id):
                    continue
                else:
                    value = ObjetoObra.objects.get(id__exact=validated_data['id_objeto'])
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class ResumenContratacionSerializer(ModelSerializer):
    list_informe_contratacion = ListField(required=False)

    class Meta:
        model = ResumenContratacion
        fields = '__all__'

    def create(self, validated_data):
        resumen = ResumenContratacion.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_informe_contratacion' in validated_data and validated_data['list_informe_contratacion']:
            list_informe_contratacion = InformeContratacion.objects.filter(id__in=validated_data['list_informe_contratacion'])
            resumen.informecontratacion_set.add(*list_informe_contratacion)
            resumen.save()

        return resumen

    def update(self, instance: ResumenContratacion, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_informe_contratacion' in validated_data:
            list_inf = InformeContratacion.objects.filter(id__in=validated_data['list_informe_contratacion'])
            instance.informecontratacion_set.add(*list_inf)

        instance.save()
        return instance


class EntidadInversionistaSerializer(ModelSerializer):
    list_contrato = ListField(required=False)

    class Meta:
        model = EntidadInversionista
        fields = '__all__'

    def create(self, validated_data):
        subcontrata = EntidadInversionista.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and validated_data['list_contrato']:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            subcontrata.contrato_set.add(*list_contrato)
            subcontrata.save()

        return subcontrata

    def update(self, instance: EntidadInversionista, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data:
            list_cont = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_cont)

        instance.save()
        return instance


class OrganismoSerializer(ModelSerializer):
    list_contrato = ListField(required=False)

    class Meta:
        model = Organismo
        fields = '__all__'

    def create(self, validated_data):
        org = Organismo.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and validated_data['list_contrato']:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            org.contrato_set.add(*list_contrato)
            org.save()

        return org

    def update(self, instance: Organismo, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data:
            list_cont = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_cont)

        instance.save()
        return instance


class ContratoSerializer(ModelSerializer):
    id_informe_geipi = IntegerField(required=False)
    id_entidad_inversionista = IntegerField(required=False)
    id_organismo = IntegerField(required=False)
    id_resumen_contabilidad = IntegerField(required=False)
    id_informe_contratacion = IntegerField(required=False)
    id_subcontrata = IntegerField(required=False)
    id_supl_cont = IntegerField(required=False)
    list_suplemento = ListField(required=False)
    list_area_ejecutora = ListField(required=False)

    class Meta:
        model = Contrato
        fields = '__all__'

    def create(self, validated_data):
        if 'id_informe_geipi' in validated_data and validated_data['id_informe_geipi']:
            validated_data['informe_geipi'] = InformeGEIPI.objects.get(id_exact=validated_data['id_informe_geipi'])

        if 'id_entidad_inversionista' in validated_data and validated_data['id_entidad_inversionista']:
            validated_data['inversionista'] =EntidadInversionista.objects.get(id_exact=validated_data['id_entidad_inversionista'])

        if 'id_organismo' in validated_data and validated_data['id_organismo']:
            validated_data['organismo'] =Organismo.objects.get(id_exact=validated_data['id_organismo'])

        if 'id_resumen_contabilidad' in validated_data and validated_data['id_resumen_contabilidad']:
            validated_data['resumen_contabilidad'] =RegistroContabilidad.objects.get(id_exact=validated_data['id_resumen_contabilidad'])

        if 'id_informe_contratacion' in validated_data and validated_data['id_informe_contratacion']:
            validated_data['informe_contratacion'] =InformeContratacion.objects.get(id_exact=validated_data['id_informe_contratacion'])

        if 'id_subcontrata' in validated_data and validated_data['id_subcontrata']:
            validated_data['subcontrata'] =Subcontrata.objects.get(id_exact=validated_data['id_subcontrata'])

        if 'id_supl_cont' in validated_data and validated_data['id_supl_cont']:
            validated_data['supl_cont'] = SuplementoContrato.objects.get(id__exact=validated_data['id_supl_cont'])

        cont = Contrato.objects.create(**get_fields_serializer(self.Meta.model, validated_data))
        change = False

        if 'list_suplemento' in validated_data:
            list_supl = Suplemento.objects.filter(id__in=validated_data['list_suplemento'])
            cont.suplemento_set.add(*list_supl)
            change = True

        if 'list_area_ejecutora' in validated_data:
            list_area = AreaEjecutora.objects.filter(id__in=validated_data['list_area_ejecutora'])
            cont.areaejecutora_set.add(*list_area)
            change = True

        if change is True:
            cont.save()

        return cont

    def update(self, instance: Contrato, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr == 'informe_geipi':
                if 'id_informe_geipi' not in validated_data or (instance.informe_geipi and validated_data['id_informe_geipi'] == instance.informe_geipi.id):
                    continue
                else:
                    value = InformeGEIPI.objects.get(id__exact=validated_data['id_informe_geipi'])
            if attr == 'inversionista':
                if not 'id_entidad_inversionista' in validated_data or (instance.inversionista and validated_data['id_entidad_inversionista'] == instance.inversionista.id):
                    continue
                else:
                    value = EntidadInversionista.objects.get(id__exact=validated_data['id_entidad_inversionista'])
            if attr == 'organismo':
                if 'id_organismo' not in validated_data or (instance.organismo and validated_data['id_organismo'] == instance.organismo.id):
                    continue
                else:
                    value = Organismo.objects.get(id__exact=validated_data['id_organismo'])
            if attr == 'resumen_contabilidad':
                if 'id_resumen_contabilidad' not in validated_data or (instance.resumen_contabilidad and validated_data['id_resumen_contabilidad'] == instance.resumen_contabilidad.id):
                    continue
                else:
                    value = RegistroContabilidad.objects.get(id__exact=validated_data['id_resumen_contabilidad'])
            if attr == 'informe_contratacion':
                if 'id_informe_contratacion' not in validated_data or (instance.informe_contratacion and validated_data['id_informe_contratacion'] == instance.informe_contratacion.id):
                    continue
                else:
                    value = InformeContratacion.objects.get(id__exact=validated_data['id_informe_contratacion'])
            if attr == 'subcontrata':
                if 'id_subcontrata' not in validated_data or (instance.subcontrata and validated_data['id_subcontrata'] == instance.subcontrata.id):
                    continue
                else:
                    value = Subcontrata.objects.get(id__exact=validated_data['id_subcontrata'])
            if attr == 'supl_cont':
                if 'id_supl_cont' not in validated_data or (instance.supl_cont and validated_data['id_supl_cont'] == instance.supl_cont.id):
                    continue
                else:
                    value = SuplementoContrato.objects.get(id__exact=validated_data['id_supl_cont'])
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_suplemento' in validated_data:
            list_supl = Suplemento.objects.filter(id__in=validated_data['list_suplemento'])
            instance.suplemento_set.add(*list_supl)

        if 'list_area_ejecutora' in validated_data:
            list_area = AreaEjecutora.objects.filter(id__in=validated_data['list_area_ejecutora'])
            instance.areaejecutora_set.add(*list_area)

        instance.save()
        return instance


class SubContrataSerializer(ModelSerializer):
    list_contrato = ListField(required=False)

    class Meta:
        model = Subcontrata
        fields = '__all__'

    def create(self, validated_data):
        subcontrata = Subcontrata.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and validated_data['list_contrato']:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            subcontrata.contrato_set.add(*list_contrato)
            subcontrata.save()

        return subcontrata

    def update(self, instance: Subcontrata, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data:
            list_cont = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_cont)

        instance.save()
        return instance


class SuplContSerializer(ModelSerializer):
    list_contratos = ListField(required=False)

    class Meta:
        model = SuplementoContrato
        fields = '__all__'

    def create(self, validated_data):
        supl_cont = SuplementoContrato.objects.create(**get_fields_serializer(self.Meta.model, validated_data))
        if 'list_contratos' in validated_data and len(validated_data['list_contratos']) > 0:
            list_contratos = Contrato.objects.filter(id__in=validated_data['list_contratos'])
            supl_cont.contrato_set.add(list_contratos)
            supl_cont.save()
        return supl_cont

    def update(self, instance: SuplementoContrato, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contratos' in validated_data:
            list_cont = Contrato.objects.filter(id__in=validated_data['list_contratos'])
            instance.contrato_set.add(*list_cont)

        instance.save()
        return instance
