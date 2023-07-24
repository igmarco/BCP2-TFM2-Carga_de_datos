import mysql.connector
import json

from cassandra import ConsistencyLevel
from cassandra.query import BatchStatement


def construccion_sqlquery(estructura):
    """
    Función general para la construcción de una consulta SQL en base a una estructura.

    Parameters
    ----------
    estructura : dict
        diccionario con el sistema de datos correspondiente a la estructura geográfica concreta
    """

    sql = "SELECT "
    for campo in estructura['campos']:
        if campo in estructura['using']:
            sql += estructura['tablas'][estructura['using'].index(campo)] + '.' + campo + ', '
        else:
            sql += campo + ', '
    sql = sql[:-2]

    sql += " FROM " + estructura['tablas'][0]
    for i, campo in enumerate(estructura['tablas'][1:]):
        # sql += ' LEFT JOIN ' + campo + " USING (" + conexion['using'][i] + ")"
        sql += ' LEFT JOIN ' + campo + " ON " + estructura['tablas'][i] + "." + estructura['using'][
            i] + " = " + campo + "." + estructura['using'][i]

    sql += " ORDER BY "
    for campo in estructura['orderby']:
        if campo in estructura['using']:
            sql += estructura['tablas'][estructura['using'].index(campo)] + '.' + campo + ', '
        else:
            sql += campo + ', '
    sql = sql[:-2]

    print(sql)

    return sql

def construccion_subregions(estructura, cursor):
    """
    Exctracción de las subregiones correspondientes con una estructura indicada a partir de un cursor con registros
    obtenidos mediante la ejecución de una consulta confeccionada a través de la estructura.

    Parameters
    ----------
    estructura : dict
        diccionario con el sistema de datos correspondiente a la estructura geográfica concreta
    cursor : object
        cursor de conexión con la base de datos que almacena los registros de las subregiones
    """

    subregions = dict()

    for x in cursor:
        # print(x)
        if len(estructura['campo_lista'].split('.')) > 1:
            campo_lista_sin_tabla = estructura['campo_lista'].split('.')[-1]
        else:
            campo_lista_sin_tabla = estructura['campo_lista']

        if x[estructura['campo_id']] in subregions:
            if x[campo_lista_sin_tabla] is not None and x[campo_lista_sin_tabla] not in subregions[x[estructura['campo_id']]][estructura['campo_lista']]:
                subregions[x[estructura['campo_id']]][estructura['campo_lista']].append(x[campo_lista_sin_tabla])
        else:
            if x[campo_lista_sin_tabla] is not None:
                subregions[x[estructura['campo_id']]] = {estructura['campo_lista']: [x[campo_lista_sin_tabla]]}
            else:
                subregions[x[estructura['campo_id']]] = {estructura['campo_lista']: []}

    # print(subregions)

    return subregions

def construccion_regions(estructura, cursor):
    """
    Exctracción de las regiones correspondientes con una estructura indicada a partir de un cursor con registros
    obtenidos mediante la ejecución de una consulta confeccionada a través de la estructura.

    Parameters
    ----------
    estructura : dict
        diccionario con el sistema de datos correspondiente a la estructura geográfica concreta
    cursor : object
        cursor de conexión con la base de datos que almacena los registros de las regiones
    """

    regions = dict()

    for x in cursor:
        subregistro = dict()
        for campo in estructura['campos']:
            if campo != estructura['campo_id'] and x[campo] is not None:
                subregistro[campo] = x[campo]
        if x[estructura['campo_id']] in regions and subregistro not in regions[x[estructura['campo_id']]]:
            regions[x[estructura['campo_id']]].append(subregistro)
        else:
            regions[x[estructura['campo_id']]] = [subregistro]

    # print(regions)

    return regions

def decode_json(introducido):
    """
    Decodificación de una cadena JSON procedente de Redis.

    Parameters
    ----------
    introducido : str
        cadena JSON procedente de Redis
    """

    lista = introducido.decode('utf-8').replace('\'', '"')
    return json.loads(lista)

def carga_subregions_redis(estructura, region_name, region_data, redis_connection):
    """
    Carga de subregiones a la base de datos de Redis para un nombre de región concreto.

    Parameters
    ----------
    estructura : dict
        diccionario con el sistema de datos correspondiente a la estructura geográfica concreta
    region_name : str
        nombre de la región
    region_data : dict
        datos asociados a la región (nombres de subregiones)
    redis_connection : object
        conexión con la BD Redis
    """

    introducido = redis_connection.get(estructura['nombre'] + ':' + region_name)
    if introducido is None:
        redis_connection.set(estructura['nombre'] + ':' + region_name, str(region_data[estructura['campo_lista']]))
    else:
        # print('ADVERTENCIA - Datos añadidos a un registro ya existente')
        lista = decode_json(introducido)
        lista.extend(region_data[estructura['campo_lista']])

        redis_connection.set(estructura['nombre'] + ':' + region_name, str(lista))

def carga_regions_redis(estructura, region_name, region_data, redis_connection):
    """
    Carga de regiones a la base de datos de Redis para un nombre de región concreto.

    Parameters
    ----------
    estructura : dict
        diccionario con el sistema de datos correspondiente a la estructura geográfica concreta
    region_name : str
        nombre de la región
    region_data : dict
        datos asociados al nombre de región (información de las regiones)
    redis_connection : object
        conexión con la BD Redis
    """

    introducido = redis_connection.get(estructura['nombre'] + ':' + str(region_name))
    if introducido is None:
        redis_connection.set(estructura['nombre'] + ':' + str(region_name), str(region_data))
    else:
        # print('ADVERTENCIA - Datos añadidos a un registro ya existente')
        lista = decode_json(introducido)
        elementos_incluidos = [elemento[estructura['campo_lista']] for elemento in lista]
        lista_nueva_str = [elemento for elemento in region_data if
                           elemento[estructura['campo_lista']] not in elementos_incluidos]
        lista.extend(lista_nueva_str)

        redis_connection.set(estructura['nombre'] + ':' + region_name, str(lista))

def carga_cassandra(estructura, cursor, session):
    """
    Carga de subregiones a la base de datos de Cassandra a partir de un cursor con registros
    obtenidos mediante la ejecución de una consulta confeccionada a través de la estructura.

    Parameters
    ----------
    estructura : dict
        diccionario con el sistema de datos correspondiente a la estructura geográfica concreta
    cursor : object
        cursor relativo a la conexión con la BD MySQL
    session : object
        sesión relativa a la conexión con la BD Cassandra
    """

    for x in cursor:
        # print(x)
        if x[estructura['campo_lista']] is not None and x[estructura['campo_id']] is not None:
            cql = "INSERT INTO " + "prueba." + estructura['nombre'] + " ("
            for campo in estructura['campos']:
                if len(campo.split('.')) > 1:
                    campo = campo.split('.')[1]
                cql += campo + ", "
            cql = cql[:-2]
            cql += ") VALUES ("
            values = []
            for campo in estructura['campos']:
                if len(campo.split('.')) > 1:
                    campo = campo.split('.')[1]
                # cql += x[campo] + ", "
                cql += "?" + ", "
                values.append(x[campo])
            cql = cql[:-2]
            cql += ") IF NOT EXISTS"

            # print(cql, values)
            pStatement = session.prepare(cql)
            session.execute(pStatement, values)

# Con el anterior método la carga se hace completamente lenta. Vamos a ver cómo arreglarlo.
def carga_cassandra_compacta(estructura, cursor, session):
    """
    Carga de subregiones a la base de datos de Cassandra a partir de un cursor con registros
    obtenidos mediante la ejecución de una consulta confeccionada a través de la estructura.
    Versión acelerada con la consideración de un batch de 100 elementos.

    Parameters
    ----------
    estructura : dict
        diccionario con el sistema de datos correspondiente a la estructura geográfica concreta
    cursor : object
        cursor relativo a la conexión con la BD MySQL
    session : object
        sesión relativa a la conexión con la BD Cassandra
    """

    cql = "INSERT INTO " + "prueba." + estructura['nombre'] + " ("
    for campo in estructura['campos']:
        if len(campo.split('.')) > 1:
            campo = campo.split('.')[1]
        cql += campo + ", "
    cql = cql[:-2]
    cql += ") VALUES ("
    values = []
    for campo in estructura['campos']:
        if len(campo.split('.')) > 1:
            campo = campo.split('.')[1]
        # cql += x[campo] + ", "
        cql += "?" + ", "
    cql = cql[:-2]
    cql += ")"

    print(cql)

    pStatement = session.prepare(cql)
    batch = BatchStatement()

    i = 0
    BATCH_MAX_SIZE = 100

    for x in cursor:
        # print(x)
        if x[estructura['campo_lista']] is not None and x[estructura['campo_id']] is not None:
            values = []
            for campo in estructura['campos']:
                if len(campo.split('.')) > 1:
                    campo = campo.split('.')[1]
                values.append(x[campo])

            # print(values)
            batch.add(pStatement, tuple(values))

            i += 1

        if i >= BATCH_MAX_SIZE:
            # print('Batch lleno.')
            session.execute(batch)
            batch.clear()
            i = 0

    if i < BATCH_MAX_SIZE:
        session.execute(batch)
