import re

def correccion_numero_detalle(num_detalle):
    if re.match('^Km', num_detalle):
        splitted = num_detalle.split(' ')
        if splitted[1].isdigit():
            numero = splitted[1]
            detalle = num_detalle.replace(' ' + numero + ' ', '')
        else:
            # print('Advertencia: \'Km\' sin número')
            numero = None
            detalle = num_detalle

    elif re.match('^Sin Número', num_detalle):
        numero = None
        detalle = None
        # print('Advertencia: Sin número ni detalle')

    else:
        if len(num_detalle.split(' ')[0].split('-')) > 1:
            numero = None
            detalle = num_detalle
        else:
            numero = num_detalle.split(' ')[0]
            detalle = (num_detalle.split(' ')[1] if len(num_detalle.split(' ')) > 1 else None)

    return numero, detalle

def estandarizar_TipoVia(tipovia):

    if tipovia == 'No':
        tipovia = 'No definido'

    return tipovia

tipo_via_index = {
    'No definido':0,
    'Boulevard':1,
    'Avenida':2,
    'Camino':3,
    'Calle':4,
    'Plaza':5,
    'Travesía':6,
    'Carretera':7,
    'Senda':8,
    'Lugar':9,
    'Barrio':10,
    'Trasera':11,
    'Callejón':12,
    'Calleja':13,
    'Polígono':14,
    'Parque':15,
    'Paseo':16,
    'Circunvalación':17,
    'Diseminado':18,
    'Pasaje':19,
    'Bajada':20,
    'Barranco':21,
    'Vía':22,
    'Grupo':23,
    'Urbanización':24,
    'Prolongación':25,
    'Cuesta':26,
    'Plazuela':27,
    'Glorieta':28,
    'Portillo':29,
    'Subida':30,
    'Acceso':31,
    'Tránsito':32,
    'Agrupación':33,
    'Puente':34,
    'Pasadizo':35,
    'Mirador':36,
    'Paraje':37,
    'Jardín':38,
    'Plazoleta':39,
    'Jardines':40,
    'Era':41,
    'Aldea':42,
    'Carretil':43
}