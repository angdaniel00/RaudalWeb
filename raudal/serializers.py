from .models import *
from .util.util import get_fields_serializer
from rest_framework.utils import model_meta
from rest_framework.serializers import ModelSerializer, IntegerField, ListField, FloatField


class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


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
    list_contrato = ListField(required=False)

    class Meta:
        model = ResumenGEIPI
        fields = '__all__'

    def create(self, validated_data):
        resumen = ResumenGEIPI.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and len(validated_data['list_contrato']) > 0:
            list_contratos = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            resumen.contrato_set.add(*list_contratos)
            resumen.save()

        return resumen

    def update(self, instance: ResumenGEIPI, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data:
            list_inf = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_inf)

        instance.save()
        return instance


class InfProduccionSerializer(ModelSerializer):
    list_contrato = ListField(required=False)

    class Meta:
        model = InformeProduccion
        fields = '__all__'

    def create(self, validated_data):
        inf = InformeProduccion.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and len(validated_data['list_contrato']) > 0:
            list_contratos = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            inf.contrato_set.add(*list_contratos)
            inf.save()

        return inf

    def update(self, instance: InformeProduccion, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data:
            list_inf = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_inf)

        instance.save()
        return instance


class PlanPreparacionObrasSerializer(ModelSerializer):
    list_contrato = ListField(required=False)

    class Meta:
        model = PlanPreparacionObras
        fields = '__all__'

    def create(self, validated_data):
        plan = PlanPreparacionObras.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data and len(validated_data['list_contrato']) > 0:
            list_contratos = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            plan.contrato_set.add(*list_contratos)
            plan.save()

        return plan

    def update(self, instance: PlanPreparacionObras, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                pass
            else:
                setattr(instance, attr, value)

        if 'list_contrato' in validated_data:
            list_contratos = Contrato.objects.filter(id__in=validated_data['list_contratos'])
            instance.contrato_set.add(*list_contratos)

        instance.save()
        return instance


class AreaEjecutoraSerializer(ModelSerializer):

    class Meta:
        model = AreaEjecutora
        fields = '__all__'


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

    class Meta:
        model = Observacion
        fields = '__all__'


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

    class Meta:
        model = InformeContratacion
        fields = '__all__'

    def create(self, validated_data):
        inf = InformeContratacion.objects.create(**get_fields_serializer(self.Meta.model, validated_data))

        if 'list_contrato' in validated_data:
            list_contrato = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            inf.contrato_set.add(*list_contrato)
            inf.save()

        return inf

    def update(self, instance: InformeContratacion, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
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

    class Meta:
        model = Suplemento
        fields = '__all__'


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

    class Meta:
        model = EntidadInversionista
        fields = '__all__'


class OrganismoSerializer(ModelSerializer):

    class Meta:
        model = Organismo
        fields = '__all__'


class ContratoSerializer(ModelSerializer):
    list_suplemento = ListField(required=False)
    list_area_ejecutora = ListField(required=False)

    class Meta:
        model = Contrato
        fields = '__all__'

    def create(self, validated_data):
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
    list_contrato = ListField(required=False)

    class Meta:
        model = SuplementoContrato
        fields = '__all__'

    def create(self, validated_data):
        supl_cont = SuplementoContrato.objects.create(**get_fields_serializer(self.Meta.model, validated_data))
        if 'list_contrato' in validated_data and len(validated_data['list_contrato']) > 0:
            list_contratos = Contrato.objects.filter(id__in=validated_data['list_contrato'])
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

        if 'list_contrato' in validated_data:
            list_cont = Contrato.objects.filter(id__in=validated_data['list_contrato'])
            instance.contrato_set.add(*list_cont)

        instance.save()
        return instance
