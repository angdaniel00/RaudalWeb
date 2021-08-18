from .util import __get_areas


def get_serializer_inf_plan_prep_obras(contratos, year):
    return {
        'year': year,
        'contratos': __get_contratos(contratos)
    }


def __get_contratos(contratos):
    list_contratos = []
    for contrato in contratos:
        list_contratos.append(__cont_ppo(contrato))
    return list_contratos


def __get_cont_ppo(list_areas):
    out = {}
    for value in list_areas:
        out[value['area']] = value['total_ejecutar_year_actual']
    return out


def __cont_ppo(contrato):
    out = {
        'no': contrato.id,
        'contrato': contrato.no_contrato,
        'nombre': contrato.name,
        'valor_contratado': __get_cont_ppo(__get_areas(contrato.areaejecutora_set.iterator(), contrato)) if contrato.areaejecutora_set else None
    }
    return out


def __get_subcontrata(type='normal', no=None, no_contrato=None, prov=None, organismo=None, clasificacion = None,  provedor=None,
                      fecha_inicio=None, fecha_terminacion=None, valor_total_cont=None, total_ejecutado=None, valor_pendiente=None,
                      valor_contratado_mp=None, valor_ejecutado_amp=None, valor_pendiente2=None, ejecucion=None):
    return {
        'type': type,
        'no': no,
        'no_contrato': no_contrato,
        'clasificacion': clasificacion,
        'provincia': prov,
        'organismo': organismo,
        'provedor': provedor,
        'fecha_inicio': fecha_inicio,
        'fecha_terminacion': fecha_terminacion,
        'valor_total_cont': valor_total_cont,
        'total_ejecutado': total_ejecutado,
        'valor_pendiente': valor_pendiente,
        'valor_contratado_mp': valor_contratado_mp,
        'valor_ejecutado_amp': valor_ejecutado_amp,
        'valor_pendiente2': valor_pendiente2,
        'ejecucion': ejecucion
    }


def __get_items_subcontrata_serializer(contratos, prov):
    list_items = []
    resumen_total_ejecutado = 0
    resumen_total_contratado = 0
    resumen_pendiente = 0
    for contrato in contratos:
        areas = contrato.areaejecutora_set.filter(objeto_obra__provincia=prov)
        total_ejecutado = 0
        total_contratado = 0
        pendiente = 0
        for area in areas:
            total_contratado += area.total_contratado
            total_ejecutado += area.total_ejecutado
            pendiente += area.total_pendiente_ejecutar
        sub = __get_subcontrata(no=contrato.id, no_contrato=contrato.no_contrato, clasificacion=contrato.clasificacion,
                                organismo=contrato.organismo.name if contrato.organismo else None,
                                fecha_inicio=contrato.fecha_inicio, fecha_terminacion=contrato.fecha_terminacion,
                                prov=prov, provedor=contrato.inversionista.name if contrato.inversionista else None,
                                valor_total_cont=total_contratado, total_ejecutado=total_ejecutado, valor_pendiente=pendiente,
                                valor_contratado_mp=total_contratado/1000, valor_ejecutado_amp=total_ejecutado/1000,
                                valor_pendiente2=pendiente, ejecucion=(total_ejecutado/total_contratado)*100)
        resumen_total_ejecutado += total_ejecutado
        resumen_total_contratado += total_contratado
        resumen_pendiente += pendiente
        list_items.append(sub)
    list_items.append(__get_subcontrata(type='resumen', valor_total_cont=resumen_total_contratado, total_ejecutado=resumen_total_ejecutado,
                                        valor_pendiente=resumen_pendiente, ejecucion=(resumen_total_ejecutado/resumen_total_contratado)*100))
    return list_items


def get_serializer_subcontrata(subcontrata, prov):
    return {
        'year': subcontrata.year,
        'mes': subcontrata.mes,
        'empresa': subcontrata.empresa,
        'update_year': subcontrata.update_year,
        'items': __get_items_subcontrata_serializer(subcontrata.contrato_set.iterator(), prov)
    }


def __get_item_inf_prod(no=None, no_contrato=None, orden=None, valor_ant=0, valor_actual=0, enero=0, febrero=0, marzo=0,
                        abril=0, mayo=0, junio=0, julio=0, agosto=0, septiembre=0, octubre=0, noviembre=0, diciembre=0,
                        ejecucion=None, pendiente=None, cliente=None):
    psemestre = enero + febrero + marzo
    ssemestre = abril + mayo + junio
    tsemestre = julio + agosto + septiembre
    csemestre = octubre + noviembre + diciembre
    return {
        'no': no,
        'contrato': no_contrato,
        'orden_trabajo': orden,
        'valor_total': valor_ant + valor_actual,
        'valor_ant': valor_ant,
        'valor_actual': valor_actual,
        'enero': enero,
        'febrero': febrero,
        'marzo': marzo,
        'psemestre': psemestre,
        'abril': abril,
        'mayo': mayo,
        'junio': junio,
        'ssemestre': abril + mayo + junio,
        'julio': julio,
        'agosto': agosto,
        'septiembre': septiembre,
        'tsemestre': tsemestre,
        'ocutbre': octubre,
        'noviembre': noviembre,
        'diciembre': diciembre,
        'csemestre': csemestre,
        'total': psemestre + ssemestre + tsemestre + csemestre,
        'ejecucion': ejecucion,
        'prod_pendiente': pendiente,
        'cliente': cliente
    }


def get_serializer_inf_produccion(inf, year):
    pass
