from django.db import models
from .util.util import get_area_resumen
import math


class SuplementoContrato(models.Model):
    empresa = models.CharField(max_length=250, default='')
    year = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)


class Cliente(models.Model):
    name = models.CharField(default='', max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)


class ResumenGEIPI(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class Cierre(models.Model):
    acumulado = models.FloatField(default=0)
    mes = models.PositiveIntegerField(default=None)
    year = models.PositiveIntegerField(default=None)
    created = models.DateTimeField(auto_now_add=True)


class PlanPreparacionObras(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class Subcontrata(models.Model):
    empresa = models.CharField(max_length=250, default='')
    mes = models.PositiveIntegerField(default=None)
    year = models.PositiveIntegerField(default=None)
    update_year = models.PositiveIntegerField(default=None)
    created = models.DateTimeField(auto_now_add=True)


class EntidadInversionista(Cliente):

    def __query_set(self, year):
        return self.areaejecutora_set.filter(year=year, contrato__areaejecutora__cliente_id__exact=self.id)

    def cant_contratos(self, year):
        return len(self.contrato_set.filter(year=year))

    def total_cuc_contratado(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cuc_contratado
        return total

    def total_cup_contratado(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cup_contratado
        return total

    def total_contratado(self, year):
        return self.total_cuc_contratado(year) + self.total_cup_contratado(year)

    def total_cuc_year_post(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cuc_valores_contratados_year_post
        return total

    def total_cup_year_post(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cup_valores_contratados_year_post
        return total

    def total_year_post(self, year):
        return self.total_cuc_year_post(year) + self.total_cup_year_post(year)

    def total_cuc_pendiente_ejecutar(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cuc_pendiente_ejecutar
        return total

    def total_cup_pendiente_ejecutar(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cup_pendiente_ejecutar
        return total

    def total_pendiente_ejecutar(self, year):
        return self.total_cuc_pendiente_ejecutar(year) + self.total_cup_pendiente_ejecutar(year)

    def total_valores_cuc_contratados_year_post(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cuc_valores_contratados_year_post
        return total

    def total_valores_cup_contratados_year_post(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cuc_valores_contratados_year_post
        return total

    def total_valores_contratados_year_post(self, year):
        return self.total_valores_cuc_contratados_year_post(year) + self.total_valores_cup_contratados_year_post(year)

    def total_cuc_contratado_year_actual(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cuc_ejecutar_year_actual
        return total

    def total_cup_contratado_year_actual(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cup_ejecutar_year_actual
        return total

    def total_contratado_year_actual(self, year):
        return self.total_cuc_contratado_year_actual(year) + self.total_cup_contratado_year_actual(year)

    def total_cuc_ejecutado_year_actual(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cuc_ejecutado_year_actual
        return total

    def total_cup_ejecutado_year_actual(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.cup_ejecutado_year_actual
        return total

    def total_ejecutado_year_actual(self, year):
        return self.total_cuc_ejecutado_year_actual(year) + self.total_cup_ejecutado_year_actual(year)

    def total_cuc_ejecutado(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.total_cuc_ejecutado
        return total

    def total_cup_ejecutado(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.total_cup_ejecutado
        return total

    def total_ejecutado(self, year):
        return self.total_cuc_ejecutado(year) + self.total_cup_ejecutado(year)

    def total_cuc_saldo_contrato(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.total_saldo_cuc_contrato
        return total

    def total_cup_saldo_contrato(self, year):
        list_area = self.__query_set(year)
        total = 0
        for area in list_area:
            total += area.total_saldo_cup_contrato
        return total

    def total_saldo_contrato(self, year):
        return self.total_cuc_saldo_contrato(year) + self.total_cup_saldo_contrato(year)


class Organismo(models.Model):
    name = models.CharField(max_length=250, default='', unique=True)
    created = models.DateTimeField(auto_now_add=True)


class ResumenContratacion(models.Model):
    name = models.CharField(max_length=250, default='')
    empresa1 = models.CharField(max_length=250, default='')
    empresa2 = models.CharField(max_length=250, default='')
    created = models.DateTimeField(auto_now_add=True)


class InformeContratacion(models.Model):
    name = models.CharField(max_length=250, default='')
    year = models.PositiveIntegerField(default=None)
    resumen = models.ForeignKey(ResumenContratacion, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(PlanPreparacionObras, on_delete=models.CASCADE, null=True)
    resumenGEIPI = models.ForeignKey(ResumenGEIPI, on_delete=models.CASCADE, null=True)
    cierre = models.OneToOneField(Cierre, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)


class ObjetoObra(models.Model):
    objeto = models.CharField(max_length=250, default='')
    ejecucion = models.CharField(max_length=250, default='')
    provincia = models.CharField(max_length=250, default='')
    tipo = models.CharField(max_length=250, default='')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_observaciones(self):
        out = ""
        for obs in self.observacion_set.iterator():
            out += (obs.observacion+" \n ")
        return out


class RegistroContabilidad(models.Model):
    empresa = models.CharField(max_length=250, default='')
    name = models.CharField(max_length=250, default='')
    mes = models.CharField(max_length=50, default='')
    autor = models.CharField(max_length=250, default='')
    fecha_elaboracion = models.DateField()
    created = models.DateTimeField(auto_now_add=True)


class InformeGEIPI(models.Model):
    provincia = models.CharField(max_length=250, default='')
    empresa = models.CharField(max_length=250, default='')
    plan_anual = models.PositiveIntegerField(default=None)
    created = models.DateTimeField(auto_now_add=True)


class Contrato(models.Model):
    name = models.CharField(max_length=250, default='')
    #no_contrato = models.CharField(max_length=250, unique=False, null=True, blank=True)
    firma = models.DateField()
    year = models.PositiveIntegerField(default=0)
    cup = models.FloatField(default=0)
    cuc = models.FloatField(default=0)
    fecha_inicio = models.DateField()
    fecha_terminacion = models.DateField()
    estado = models.CharField(max_length=25, default='')
    clasificacion = models.CharField(max_length=250, default='')
    resumen_contabilidad = models.ForeignKey(RegistroContabilidad, on_delete=models.NOT_PROVIDED, null=True)
    informe_contratacion = models.ForeignKey(InformeContratacion, on_delete=models.NOT_PROVIDED, null=True)
    informe_geipi = models.ForeignKey(InformeGEIPI, on_delete=models.NOT_PROVIDED, null=True)
    inversionista = models.ForeignKey(EntidadInversionista, on_delete=models.CASCADE, null=True)
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE, null=True)
    subcontrata = models.ForeignKey(Subcontrata, on_delete=models.CASCADE, null=True)
    supl_cont = models.ForeignKey(SuplementoContrato, on_delete=models.NOT_PROVIDED, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def valor_inicial(self):
        return self.cuc + self.cup

    @property
    def cuc_resumen(self):
        cont = self.cup
        for supl in self.suplemento_set.iterator():
            cont += supl.cuc
        return cont

    @property
    def cup_resumen(self):
        cont = self.cup
        for supl in self.suplemento_set.iterator():
            cont += supl.cup
        return cont

    @property
    def total_resumen(self):
        return self.cuc + self.cup_resumen

    @property
    def total_cuc(self):
        total = 0
        for supl in self.suplemento_set.iterator():
            total += supl.cuc
        return total

    @property
    def total_cup(self):
        total = 0
        for supl in self.suplemento_set.iterator():
            total += supl.cup
        return total

    @property
    def cant_supl(self):
        return self.suplemento_set.count()

    @property
    def resumen_area(self):
        total_contratado = 0
        total_contratado_year_ant = 0
        total_pendiente_ejecutar = 0
        total_ejecutado_year_ant = 0
        total_year_post = 0
        total_ejecutar_year_actual = 0
        total_ejecutado_year_actual = 0
        total_cuc_ejecutado = 0
        total_cup_ejecutado = 0
        total_ejecutado = 0
        total_saldo_cuc_contrato = 0
        total_saldo_cup_contrato = 0
        total_saldo_contratado = 0
        for area in self.areaejecutora_set.iterator():
            total_contratado += area.total_contratado
            total_contratado_year_ant += area.total_contratado_year_ant
            total_pendiente_ejecutar += area.total_pendiente_ejecutar
            total_year_post += area.total_year_post
            total_ejecutar_year_actual += area.total_ejecutar_year_actual
            total_ejecutado_year_actual += area.total_ejecutado_year_actual
            total_cuc_ejecutado += area.total_cuc_ejecutado
            total_cup_ejecutado += area.total_cup_ejecutado
            total_ejecutado += area.total_ejecutado
            total_saldo_cuc_contrato += area.total_saldo_cuc_contrato
            total_saldo_cup_contrato += area.total_saldo_cup_contrato
            total_saldo_contratado += area.total_saldo_contratado
            total_ejecutado_year_ant += area.total_ejecutado_year_ant
        return get_area_resumen(total_contratado=total_contratado, total_contratado_year_ant=total_contratado_year_ant,
                                total_pendiente_ejecutar=total_pendiente_ejecutar, total_year_post=total_year_post,
                                total_ejecutar_year_actual=total_ejecutar_year_actual, total_ejecutado_year_actual=total_ejecutado_year_actual,
                                total_cuc_ejecutado=total_cuc_ejecutado, total_cup_ejecutado=total_cup_ejecutado,
                                total_ejecutado=total_ejecutado, total_saldo_cuc_contrato=total_saldo_cuc_contrato,
                                total_saldo_cup_contrato=total_saldo_cup_contrato, total_saldo_contratado=total_saldo_contratado,
                                fecha_inicio=self.fecha_inicio, real_terminacion=self.fecha_terminacion,
                                total_ejecutado_year_ant=total_ejecutado_year_ant)


class AreaEjecutora(models.Model):
    area = models.CharField(max_length=250, default='')
    cup_contratado = models.FloatField(default=0)
    cuc_contratado = models.FloatField(default=0)
    cup_year_ant = models.FloatField(default=0)
    cuc_year_ant = models.FloatField(default=0)
    cup_valores_contratados_year_post = models.FloatField(default=0)
    cuc_valores_contratados_year_post = models.FloatField(default=0)
    cuc_ejecutado_year_ant = models.FloatField(default=0)
    cup_ejecutado_year_ant = models.FloatField(default=0)
    cup_ejecutado_year_actual = models.FloatField(default=0)
    cuc_ejecutado_year_actual = models.FloatField(default=0)
    fecha_inicio = models.DateField()
    pactada_terminacion = models.DateField()
    real_terminacion = models.DateField()
    year = models.PositiveIntegerField(default=None)
    pronostico = models.FloatField(default=0)
    objeto_obra = models.ForeignKey(ObjetoObra, on_delete=models.CASCADE, null=True)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def cuc_ejecutar_year_actual(self):
        return math.fabs(self.cuc_pendiente_ejecutar)

    @property
    def cup_ejecutar_year_actual(self):
        return math.fabs(self.cup_pendiente_ejecutar)

    @property
    def total_ejecutado_year_ant(self):
        return self.cuc_ejecutado_year_ant + self.cup_ejecutado_year_ant

    @property
    def cuc_pendiente_ejecutar(self):
        return self.cuc_contratado - self.cuc_ejecutado_year_ant

    @property
    def cup_pendiente_ejecutar(self):
        return self.cup_contratado - self.cup_ejecutado_year_ant

    @property
    def total_contratado(self):
        return self.cuc_contratado + self.cup_contratado

    @property
    def total_contratado_year_ant(self):
        return self.cuc_year_ant + self.cup_year_ant

    @property
    def total_pendiente_ejecutar(self):
        return self.cuc_pendiente_ejecutar + self.cup_pendiente_ejecutar

    @property
    def total_year_post(self):
        return self.cuc_valores_contratados_year_post + self.cup_valores_contratados_year_post

    @property
    def total_ejecutar_year_actual(self):
        return self.cuc_ejecutar_year_actual + self.cup_ejecutar_year_actual

    @property
    def total_ejecutado_year_actual(self):
        return self.cuc_ejecutado_year_actual + self.cup_ejecutado_year_actual

    @property
    def total_cuc_ejecutado(self):
        return self.cuc_ejecutado_year_actual + self.cuc_year_ant

    @property
    def total_cup_ejecutado(self):
        return self.cup_ejecutado_year_actual + self.cup_year_ant

    @property
    def total_ejecutado(self):
        return self.total_cuc_ejecutado + self.total_cup_ejecutado

    @property
    def total_saldo_cuc_contrato(self):
        return self.cuc_contratado - self.total_cuc_ejecutado

    @property
    def total_saldo_cup_contrato(self):
        return self.cup_contratado - self.total_cup_ejecutado

    @property
    def total_saldo_contratado(self):
        return self.total_saldo_cuc_contrato + self.total_saldo_cup_contrato


class Observacion(models.Model):
    observacion = models.CharField(max_length=250, default='')
    objeto_obra = models.ForeignKey(ObjetoObra, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Suplemento(models.Model):
    cup = models.FloatField(default=0)
    cuc = models.FloatField(default=0)
    firma = models.DateField()
    objeto = models.OneToOneField(ObjetoObra, on_delete=models.CASCADE, default=None, null=True)
    terminacion = models.DateField()
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def valor_actual_contrato_inc_supl(self):
        return self.cuc + self.cup

