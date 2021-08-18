from django.db.models import Model


prov = (
    'Pinar del Río', 'Artemisa', 'Mayabeque', 'La Habana', 'Matanzas', 'Villa Clara', 'Cienfuegos', 'Sancti Spiritus',
    'Ciego de Ávila', 'Camagüey', 'Las Tunas', 'Holguín', 'Granma', 'Santiago de Cuba', 'Guantánamo',
    'Isla de la Juventud')


def get_fields_serializer(model_class: Model, validate_data: dict):
    fields = {}
    for key in validate_data.keys():
        if hasattr(model_class, key) is True:
            fields[key] = validate_data[key]
    return fields


def get_area_resumen(area=None, cup_contratado=None, cuc_contratado=None, cup_year_ant=None, cuc_year_ant=None,
                     cup_pendiente_ejecutar=None,
                     cuc_pendiente_ejecutar=None, cup_valores_contratados_year_post=None,
                     cuc_valores_contratados_year_post=None,
                     cup_ejecutar_year_actual=None, cuc_ejecutar_year_actual=None, cup_ejecutado_year_actual=None,
                     cuc_ejecutado_year_actual=None, fecha_inicio=None, pactada_terminacion=None, real_terminacion=None,
                     year=None, pronostico=None, cliente=None, objeto_obra=None, total_contratado=None,
                     total_contratado_year_ant=None,
                     total_pendiente_ejecutar=None, total_year_post=None, total_ejecutar_year_actual=None,
                     total_ejecutado_year_actual=None,
                     total_cuc_ejecutado=None, total_cup_ejecutado=None, total_ejecutado=None,
                     total_saldo_cuc_contrato=None,
                     total_saldo_cup_contrato=None, total_saldo_contratado=None, total_ejecutado_year_ant=None):
    area: dict = {
        'type': 'normal' if area else 'total',
        'area': area if area else 'Total',
        'cup_contratado': cup_contratado,
        'cuc_contratado': cuc_contratado,
        'cup_year_ant': cup_year_ant,
        'cuc_year_ant': cuc_year_ant,
        'cup_pendiente_ejecutar': cup_pendiente_ejecutar,
        'cuc_pendiente_ejecutar': cuc_pendiente_ejecutar,
        'cup_valores_contratados_year_post': cup_valores_contratados_year_post,
        'cuc_valores_contratados_year_post': cuc_valores_contratados_year_post,
        'cup_ejecutar_year_actual': cup_ejecutar_year_actual,
        'cuc_ejecutar_year_actual': cuc_ejecutar_year_actual,
        'cup_ejecutado_year_actual': cup_ejecutado_year_actual,
        'cuc_ejecutado_year_actual': cuc_ejecutado_year_actual,
        'fecha_inicio': fecha_inicio,
        'pactada_terminacion': pactada_terminacion,
        'real_terminacion': real_terminacion,
        'year': year,
        'pronostico': pronostico,
        'cliente': cliente,
        'objeto_obra': objeto_obra,
        'total_contratado': total_contratado,
        'total_contratado_year_ant': total_contratado_year_ant,
        'total_pendiente_ejecutar': total_pendiente_ejecutar,
        'total_year_post': total_year_post,
        'total_ejecutar_year_actual': total_ejecutar_year_actual,
        'total_ejecutado_year_actual': total_ejecutado_year_actual,
        'total_cuc_ejecutado': total_cuc_ejecutado,
        'total_cup_ejecutado': total_cup_ejecutado,
        'total_ejecutado': total_ejecutado,
        'total_saldo_cuc_contrato': total_saldo_cuc_contrato,
        'total_saldo_cup_contrato': total_saldo_cup_contrato,
        'total_saldo_contratado': total_saldo_contratado,
        'total_ejecutado_year_ant': total_ejecutado_year_ant
    }

    return area


def __get_area(area, objeto=False):
    area_ejecutora: dict = {
        'area': area.area,
        'cup_contratado': area.cup_contratado,
        'cuc_contratado': area.cuc_contratado,
        'cup_year_ant': area.cup_year_ant,
        'cuc_year_ant': area.cuc_year_ant,
        'cup_pendiente_ejecutar': area.cup_pendiente_ejecutar,
        'cuc_pendiente_ejecutar': area.cuc_pendiente_ejecutar,
        'cup_valores_contratados_year_post': area.cup_valores_contratados_year_post,
        'cuc_valores_contratados_year_post': area.cuc_valores_contratados_year_post,
        'cup_ejecutar_year_actual': area.cup_ejecutar_year_actual,
        'cuc_ejecutar_year_actual': area.cuc_ejecutar_year_actual,
        'cup_ejecutado_year_actual': area.cup_ejecutado_year_actual,
        'cuc_ejecutado_year_actual': area.cuc_ejecutado_year_actual,
        'cuc_ejecutado_year_ant': area.cuc_ejecutado_year_ant,
        'cup_ejecutado_year_ant': area.cup_ejecutado_year_ant,
        'fecha_inicio': area.fecha_inicio,
        'pactada_terminacion': area.pactada_terminacion,
        'real_terminacion': area.real_terminacion,
        'year': area.year,
        'pronostico': area.pronostico,
        'objeto_obra': {},
        'total_contratado': area.total_contratado,
        'total_contratado_year_ant': area.total_contratado_year_ant,
        'total_pendiente_ejecutar': area.total_pendiente_ejecutar,
        'total_year_post': area.total_year_post,
        'total_ejecutar_year_actual': area.total_ejecutar_year_actual,
        'total_ejecutado_year_actual': area.total_ejecutado_year_actual,
        'total_cuc_ejecutado': area.total_cuc_ejecutado,
        'total_cup_ejecutado': area.total_cup_ejecutado,
        'total_ejecutado': area.total_ejecutado,
        'total_saldo_cuc_contrato': area.total_saldo_cuc_contrato,
        'total_saldo_cup_contrato': area.total_saldo_cup_contrato,
        'total_saldo_contratado': area.total_saldo_contratado,
        'total_ejecutado_year_ant': area.total_ejecutado_year_ant

    }
    return area_ejecutora


def __get_areas(areas, contrato):
    list_area: list = []
    for area in areas:
        list_area.append(__get_area(area))
    list_area.append(contrato.resumen_area)
    return list_area


def __create_supl_serializer(supl_model=None, cont=None):
    supl: dict = {
        'cuc': supl_model.cuc if supl_model else cont.cuc_resumen,
        'cup': supl_model.cup if supl_model else cont.cup_resumen,
        'firma': supl_model.firma if supl_model else None,
        'objeto': supl_model.objeto.objeto if supl_model and supl_model.objeto else None,
        'terminacion': supl_model.terminacion if supl_model else cont.fecha_terminacion,
        'contrato': supl_model.contrato.name if supl_model and supl_model.contrato else None,
        'registro': supl_model.contrato.resumen_contabilidad.name if supl_model and supl_model.contrato and supl_model.contrato.resumen_contabilidad else None,
        'valor_actual_contrato_inc_supl': supl_model.valor_actual_contrato_inc_supl if supl_model else cont.total_resumen
    }
    if cont:
        supl['name'] = 'resumen'
    return supl


def __create_suplementos(cont):
    supls = []
    for supl in cont.suplemento_set.iterator():
        s = __create_supl_serializer(supl_model=supl)
        supls.append(s)
    supls.append(__create_supl_serializer(cont=cont))
    return supls


def __get_dict_contrato(cont, area=False, supl=False):
    contrato: dict = {
        'name': cont.name,
        'no_contrato': cont.no_contrato,
        'firma': cont.firma,
        'year': cont.year,
        'cup': cont.cup,
        'cuc': cont.cuc,
        'cliente': cont.inversionista.name if cont.inversionista else None,
        'fecha_inicio': cont.fecha_inicio,
        'fecha_terminacion': cont.fecha_terminacion,
        'estado': cont.estado,
        'clasificacion': cont.clasificacion,
        'resumen_contabilidad': {},
        'informe_contratacion': {},
        'informe_geipi': {},
        'inversionista': cont.inversionista.name if cont.inversionista else None,
        'organismo': cont.organismo.name if cont.organismo else None,
        'subcontrata': {},
        'suplemento': __create_suplementos(cont) if supl is True else None,
        'valor_inicial': cont.valor_inicial,
        'total_cuc': cont.total_cuc,
        'total_cup': cont.total_cup,
        'cant_supl': cont.cant_supl,
        'valor_inicial_contratado': cont.valor_inicial,
        'areas_ejecutoras': __get_areas(cont.areaejecutora_set.iterator(), cont) if area is True else None
    }

    return contrato


def get_serializer_informe_contratacion(set_informe_contratacion: set):
    out = []
    for c in set_informe_contratacion:
        contrato = __get_dict_contrato(c, area=True)
        out.append(contrato)
    return out


def get_supl_cont_serializer(set_contrato: set):
    out = []
    for c in set_contrato:
        contrato = __get_dict_contrato(c, supl=True)
        out.append(contrato)
    return out


def __get_contrato_registro_serializer(cliente=None, no_contrato=None, valor_total=None,
                                       valor_contratado_year_actual1=None,
                                       valor_contratado_year_actual2=None, valor_contratado_year_actual3=None,
                                       fecha_inicio=None,
                                       fecha_terminacion=None, no_suplementos=None, valor_suplementos=None,
                                       observaciones=None):
    contrato: dict = {
        'cliente': cliente,
        'no_contrato': no_contrato,
        'valor_total': valor_total,
        'valor_contratado_year_actual1': valor_contratado_year_actual1,
        'valor_contratado_year_actual2': valor_contratado_year_actual2,
        'valor_contratado_year_actual3': valor_contratado_year_actual3,
        'fecha_inicio': fecha_inicio,
        'fecha_terminacion': fecha_terminacion,
        'no_suplementos': no_suplementos,
        'valor_suplementos': valor_suplementos,
        'observaciones': observaciones
    }
    return contrato


def __get_dict_contrato_registro_resumen(list_cont: list):
    valor_total = 0
    valor_contratado1 = 0
    valor_contratado2 = 0
    valor_contratado3 = 0
    cant_supl = 0
    valor_supl_total = 0
    for element in list_cont:
        valor_total += element['valor_total']
        valor_contratado1 += element['valor_contratado_year_actual1']
        valor_contratado2 += element['valor_contratado_year_actual2']
        valor_contratado3 += element['valor_contratado_year_actual3']
        cant_supl += element['no_suplementos']
        valor_supl_total += element['valor_suplementos']
    contrato = __get_contrato_registro_serializer(valor_total=valor_total,
                                                  valor_contratado_year_actual1=valor_contratado1,
                                                  valor_contratado_year_actual2=valor_contratado2,
                                                  valor_contratado_year_actual3=valor_contratado3,
                                                  no_suplementos=cant_supl, valor_suplementos=valor_supl_total)
    contrato['type'] = 'resumen'
    return contrato


def __get_dict_contrato_registro(cont, area: str):
    try:
        area_ejecutora = cont.areaejecutora_set.get(area=area)
        return __get_contrato_registro_serializer(
            cliente=cont.inversionista.name if cont.inversionista else None,
            no_contrato=cont.id,
            valor_total=area_ejecutora.total_contratado if area_ejecutora else None,
            valor_contratado_year_actual1=area_ejecutora.cup_ejecutar_year_actual if area_ejecutora else None,
            valor_contratado_year_actual2=area_ejecutora.cup_ejecutar_year_actual + area_ejecutora.cuc_ejecutar_year_actual if area_ejecutora else None,
            valor_contratado_year_actual3=area_ejecutora.cuc_ejecutar_year_actual if area_ejecutora else None,
            fecha_inicio=cont.fecha_inicio, fecha_terminacion=cont.fecha_terminacion, no_suplementos=cont.cant_supl,
            valor_suplementos=area_ejecutora.total_contratado if area_ejecutora else None,
            observaciones=area_ejecutora.objeto_obra.get_observaciones if area_ejecutora and area_ejecutora.objeto_obra else None
        )
    except:
        return None


def get_registro_contabilidad_serializer(set_contrato: set, area: str):
    out = []
    for c in set_contrato:
        contrato = __get_dict_contrato_registro(c, area)
        if contrato:
            out.append(contrato)
    out.append(__get_dict_contrato_registro_resumen(out))
    return out


def __contrato_geipi_serializer(no_contrato=None, clasificacion=None, objeto_obra=None, provincia=None, organismo=None,
                                inversionista=None, fecha_inicio=None, fecha_terminacion=None, valor_contratado=None,
                                valor_ejecutado_acumulado=None, por_ejecucion=None, resumen=False):
    contrato: dict = {
        'no_contrato': no_contrato,
        'clasificacion': clasificacion,
        'objeto_obra': objeto_obra,
        'provincia': provincia,
        'organismo': organismo,
        'inversionista': inversionista,
        'fecha_inicio': fecha_inicio,
        'fecha_terminacion': fecha_terminacion,
        'valor_contratado': valor_contratado,
        'valor_ejecutado_acumulado': valor_ejecutado_acumulado,
        'por_ejecucion': por_ejecucion
    }
    if resumen is True:
        contrato['type'] = 'resumen'
    return contrato


def __get_dict_contrato_geipi(contrato, area: str):
    try:
        area = contrato.areaejecutora_set.get(area__exact=area)
        valor_contratado = area.total_ejecutar_year_actual / 1000
        valor_ejecutado = area.total_ejecutado_year_actual / 1000
        por_ejecutado = (valor_ejecutado / valor_contratado) * 100
        return __contrato_geipi_serializer(no_contrato=None,
                                           clasificacion=area.objeto_obra.tipo if area.objeto_obra else None,
                                           objeto_obra=area.objeto_obra.objeto if area.objeto_obra else None,
                                           provincia=area.objeto_obra.provincia if area.objeto_obra else None,
                                           organismo=contrato.organismo.name if contrato.organismo else None,
                                           inversionista=contrato.inversionista.name if contrato.organismo else None,
                                           fecha_inicio=area.fecha_inicio, fecha_terminacion=area.pactada_terminacion,
                                           valor_contratado=valor_contratado, valor_ejecutado_acumulado=valor_ejecutado,
                                           por_ejecucion=por_ejecutado)
    except:
        return None


def get_informe_geipi_serializer(set_contrato: set, area: str):
    out = []
    valor_contratado = 0
    valor_ejecutado = 0
    for c in set_contrato:
        contrato = __get_dict_contrato_geipi(c, area)
        if contrato:
            valor_contratado += contrato['valor_contratado']
            valor_ejecutado += contrato['valor_ejecutado_acumulado']
            out.append(contrato)
    out.append(__contrato_geipi_serializer(valor_contratado=valor_contratado, valor_ejecutado_acumulado=valor_ejecutado,
                                           resumen=True))
    return out


def __get_contrato_prov(contratos):
    out = {}
    for cont in contratos:
        areas = cont.areaejecutora_set
        if areas:
            for p in prov:
                ars = areas.filter(objeto_obra__provincia=p)
                if ars:
                    if p in out:
                        out[p] = out[p].extend(ars.iterator())
                    else:
                        l = []
                        l.extend(ars.iterator())
                        out[p] = l
    return out


def __get_item_contrato(areas):
    ej = {}
    for area in areas:
        if area.area in ej:
            item = ej[area.area]
            item['valor_contratado'] += area.total_ejecutar_year_actual
            item['valor_ejecutado'] += area.total_ejecutado_year_actual
            item['pronostico_ejecucion'] += area.pronostico
            item['cierre_year_pro'] = item['valor_ejecutado'] + item['pronostico_ejecucion']
            item['observaciones'] += area.get_observaciones
        else:
            value = {
                'valor_contratado': area.total_ejecutar_year_actual,
                'valor_ejecutado': area.total_ejecutado_year_actual,
                'pronostico_ejecucion': area.pronostico,
                'cierre_year_pro': area.total_ejecutado_year_actual + area.pronostico,
                'observaciones': area.get_observaciones
            }
            ej[area.area] = value
    return ej


def get_resumen_geipi_serializer(contratos):
    resumen_serializer = []
    if contratos:
        contratos = __get_contrato_prov(contratos)
        for (key, value) in contratos.items():
            out1 = {
                'provincia': key,
                'items': __get_item_contrato(value)
            }
            resumen_serializer.append(out1)
    return resumen_serializer
