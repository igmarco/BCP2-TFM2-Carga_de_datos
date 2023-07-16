import mysql.connector
import pandas as pd

import util_carga_datosT1_MySQL

def bd_connection(host="localhost", user="root", password="root", database="Direcciones_LaRioja"):
    connector = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = connector.cursor(buffered=True)

    return connector, cursor

def show_tables(cursor, database=None):
    if database is not None:
        sql = "USE " + database
        cursor.execute(sql)

    cursor.execute("SHOW TABLES")

    for x in cursor:
        print(x)

def import_CSV(file, separation=','):
    # print(file)
    return pd.read_csv(file, sep=separation)

def corregir_nombres_columnas(df):
    cols = df.columns
    cols_corregidas = []
    for col in cols:
        cols_corregidas.append(col.replace('0','.'))
    df.columns = cols_corregidas

host =      "localhost"
user =      "root"
password =  "root"
database =  "Direcciones_LaRioja"

# general_path = "C:/Users/igmarco/OneDrive - Universidad de La Rioja/Escritorio/Beca de Colaboración/BCP2 (TFM2)/5. BCP2 - Preparación de datos/5.0. Datos/T1"
general_path = "../../5.0. Datos/T1"
files_names = {
    'address':  "APP_CLLRIOJA.GC_ADDRESS.csv",
    'street':   "APP_CLLRIOJA.GC_STREET.csv",
    'venues':   "APP_CLLRIOJA.GC_VENUES.csv",
    'places':   "APP_CLLRIOJA.GC_PLACES.csv"
}

files_paths = {}
for file in files_names:
    files_paths[file] = general_path + '/' + files_names[file]

# print(files_paths)

address = import_CSV(files_paths['address'], separation=',')
street =  import_CSV(files_paths['street'], separation=',')
venues =  import_CSV(files_paths['venues'], separation=',')
places =  import_CSV(files_paths['places'], separation=',')

corregir_nombres_columnas(address)
corregir_nombres_columnas(street)
corregir_nombres_columnas(venues)
corregir_nombres_columnas(places)

# print(address.columns)

dlr_db, dlr_cursor = bd_connection(host=host,
                                    user=user,
                                    password=password,
                                    database=database)
# show_tables(dlr_cursor)

def agregar_Estado(address, street, venues, places, connector, cursor):
    places_country = places[places['PLACETYPE'] == 'country']
    # print(len(places_country))
    rowcount = 0
    for ind, elem in places_country.iterrows():
        # print(estado)
        sql = "INSERT INTO Estado (idEstado, nombreEstado) VALUES (%s, %s)"
        val = (int(elem['LINEAGE.COUNTRY.ID']),
               elem['LINEAGE.COUNTRY.NAME'])
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_CA(address, street, venues, places, connector, cursor):
    places_CA = places[places['PLACETYPE'] == 'macroregion']
    # print(len(places_CA))
    rowcount = 0
    for ind, elem in places_CA.iterrows():
        # print(elem)
        sql = "INSERT INTO CA (idCA, nombreCA, idEstado) VALUES (%s, %s, %s)"
        val = (int(elem['LINEAGE.MACROREGION.ID']),
               elem['LINEAGE.MACROREGION.NAME'],
               int(elem['LINEAGE.COUNTRY.ID']))
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_Provincia(address, street, venues, places, connector, cursor):
    places_Provincia = places[places['PLACETYPE'] == 'region']
    # print(len(places_Provincia))
    rowcount = 0
    for ind, elem in places_Provincia.iterrows():
        # print(elem)
        sql = "INSERT INTO Provincia (idProvincia, nombreProvincia, idCA) VALUES (%s, %s, %s)"
        val = (int(elem['LINEAGE.REGION.ID']),
               elem['LINEAGE.REGION.NAME'],
               int(elem['LINEAGE.MACROREGION.ID']))
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

# def agregar_Comarca(address, street, venues, places, connector, cursor):
#     places_Comarca = places[places['PLACETYPE'] == '???????']
#     # print(len(places_Comarca))
#     rowcount = 0
#     for ind, elem in places_Comarca.iterrows():
#         # print(elem)
#         sql = "INSERT INTO Comarca (idComarca, nombreComarca, idProvincia) VALUES (%s, %s, %s)"
#         val = (int(elem['LINEAGE.???????.ID']),
#                elem['LINEAGE.???????.NAME'],
#                int(elem['LINEAGE.REGION.ID']))
#         cursor.execute(sql, val)
#         rowcount += cursor.rowcount
#
#     connector.commit()
#
#     print(rowcount, "record inserted.")

def agregar_Municipio(address, street, venues, places, connector, cursor):
    places_Municipio = places[places['PLACETYPE'] == 'localadmin']
    # print(len(places_Municipio))
    rowcount = 0
    for ind, elem in places_Municipio.iterrows():
        # print(elem)
        sql = "INSERT INTO Municipio (idMunicipio, nombreMunicipio, idProvincia) VALUES (%s, %s, %s)"
        val = (int(elem['LINEAGE.LOCALADMIN.ID']),
               elem['LINEAGE.LOCALADMIN.NAME'],
               int(elem['LINEAGE.REGION.ID']))
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_Nivel(address, street, venues, places, connector, cursor):
    places_Nivel = places[places['PLACETYPE'] == 'locality']
    # print(len(places_Nivel))
    rowcount = 0
    for ind, elem in places_Nivel.iterrows():
        # print(elem)
        sql = "INSERT INTO Nivel (idNivel, nombreNivel, tipoNivel) VALUES (%s, %s, %s)"
        val = (int(elem['LINEAGE.LOCALITY.ID']),
               elem['LINEAGE.LOCALITY.NAME'],
               'Población')
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_Nivel1(address, street, venues, places, connector, cursor):
    places_Nivel1 = places[places['PLACETYPE'] == 'locality']
    # print(len(places_Nivel1))
    rowcount = 0
    for ind, elem in places_Nivel1.iterrows():
        # print(elem)
        sql = "INSERT INTO Nivel1 (idNivel1, idNivel, idMunicipio) VALUES (%s, %s, %s)"
        val = (int(elem['LINEAGE.LOCALITY.ID']),
               int(elem['LINEAGE.LOCALITY.ID']),
               int(elem['LINEAGE.LOCALADMIN.ID']))
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

# def agregar_Nivel2(address, street, venues, places, connector, cursor):
#     places_Nivel2 = places[places['PLACETYPE'] == '??????']
#     # print(len(places_Nivel2))
#     rowcount = 0
#     for ind, elem in places_Nivel2.iterrows():
#         # print(elem)
#         sql = "INSERT INTO Nivel1 (idNivel2, idNivel, idNivel1) VALUES (%s, %s, %s)"
#         val = (int(elem['LINEAGE.????????.ID']),
#                int(elem['LINEAGE.????????.ID']),
#                int(elem['LINEAGE.LOCALITY.ID']))
#         cursor.execute(sql, val)
#         rowcount += cursor.rowcount
#
#     connector.commit()
#
#     print(rowcount, "record inserted.")

def agregar_TipoVia(address, street, venues, places, connector, cursor):
    places_TipoVia = street['ADDRESS_PARTS.STREET'].str.replace('\xa0', ' ').str.split(' ', n=1, expand=True)[0].unique()
    # print(len(places_TipoVia))
    rowcount = 0
    for elem in places_TipoVia:
        # print(elem)
        elem = util_carga_datosT1_MySQL.estandarizar_TipoVia(elem)
        sql = "INSERT INTO TipoVia (idTipoVia, nombreTipoVia) VALUES (%s, %s)"
        val = (util_carga_datosT1_MySQL.tipo_via_index[elem],
               elem)
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_Via(address, street, venues, places, connector, cursor):
    places_Via = street
    # print(len(places_Via))
    rowcount = 0
    for ind, elem in places_Via.iterrows():
        # print(elem)
        sql = "INSERT INTO Via (idVia, idMunicipio, idNivel1, idTipoVia, nombreVia, posicion) VALUES (%s, %s, %s, %s, %s, POINT(%s, %s))"
        val = (elem['ELASTICSEARCH_ID'],
               int(elem['PARENT.LOCALADMIN_ID']),
               int(elem['PARENT.LOCALITY_ID']),
               int(util_carga_datosT1_MySQL.tipo_via_index[util_carga_datosT1_MySQL.estandarizar_TipoVia(elem['ADDRESS_PARTS.STREET'].replace('\xa0', ' ').split(' ', 1)[0])]),
               elem['ADDRESS_PARTS.NAME'],
               elem['CENTER_POINT.LON'],
               elem['CENTER_POINT.LAT'])
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

# def agregar_ViaAntigua(address, street, venues, places, connector, cursor):
#     places_ViaAntigua = '?????'
#     # print(len(places_Via))
#     rowcount = 0
#     for ind, elem in places_ViaAntigua.iterrows():
#         # print(elem)
#         sql = "INSERT INTO ViaAntigua (idViaAntigua, idVia, nombreVia) VALUES (%s, %s, %s)"
#         val = (elem['ELASTICSEARCH_ID'],
#                elem['ELASTICSEARCH_ID'],
#                elem['ADDRESS_PARTS.NAME'])
#         cursor.execute(sql, val)
#         rowcount += cursor.rowcount
#
#     connector.commit()
#
#     print(rowcount, "record inserted.")

def agregar_Direccion(address, street, venues, places, connector, cursor):
    places_Direccion = address
    # print(len(places_Direccion))
    rowcount = 0
    for ind, elem in places_Direccion.iterrows():
        # print(elem)
        # print((elem['ELASTICSEARCH_ID'].replace('address', 'street'))[:-10])
        numero, detalle = util_carga_datosT1_MySQL.correccion_numero_detalle(elem['ADDRESS_PARTS.NUMBER'])
        sql = "INSERT INTO Direccion (idDireccion, idVia, codPostal, numero, detalle, posicion) VALUES (%s, %s, %s, %s, %s, POINT(%s, %s))"
        # sql = "INSERT INTO Direccion (idDireccion, idVia, codPostal, numero, posicion) VALUES (%s, %s, %s, %s, POINT(%s, %s))"
        val = (elem['ELASTICSEARCH_ID'],
               (elem['ELASTICSEARCH_ID'].replace('address', 'street'))[:-10],
               int(elem['ADDRESS_PARTS.ZIP']),
               # numero if numero else '-1',
               numero,
               detalle,
               elem['CENTER_POINT.LON'],
               elem['CENTER_POINT.LAT'])
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_NombrePropio(address, street, venues, places, connector, cursor):
    places_NombrePropio = venues
    # print(len(places_NombrePropio))
    rowcount = 0
    for ind, elem in places_NombrePropio.iterrows():
        # print(elem)
        sql = "INSERT INTO NombrePropio (idDireccion, nombre) VALUES (%s, %s)"
        val = (elem['ELASTICSEARCH_ID'].replace('venues', 'address'),
               elem['NAME.DEFAULT'])
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_CodPostal_Nivel(address, street, venues, places, connector, cursor):
    places_CodPostal_Nivel = address[['ADDRESS_PARTS.ZIP', 'PARENT.LOCALITY_ID']].drop_duplicates()
    # print(len(places_CodPostal_Nivel))
    rowcount = 0
    for ind, elem in places_CodPostal_Nivel.iterrows():
        # print(elem)
        sql = "INSERT INTO CodPostal_Nivel (codPostal, idNivel) VALUES (%s, %s)"
        val = (int(elem['ADDRESS_PARTS.ZIP']),
               int(elem['PARENT.LOCALITY_ID']))
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

def agregar_CodPostal_Municipio(address, street, venues, places, connector, cursor):
    places_CodPostal_Municipio = address[['ADDRESS_PARTS.ZIP', 'PARENT.LOCALADMIN_ID']].drop_duplicates()
    # print(len(places_CodPostal_Municipio))
    rowcount = 0
    for ind, elem in places_CodPostal_Municipio.iterrows():
        # print(elem)
        sql = "INSERT INTO CodPostal_Municipio (codPostal, idMunicipio) VALUES (%s, %s)"
        val = (int(elem['ADDRESS_PARTS.ZIP']),
               int(elem['PARENT.LOCALADMIN_ID']))
        cursor.execute(sql, val)
        rowcount += cursor.rowcount

    connector.commit()

    print(rowcount, "record inserted.")

agregar_Estado(address, street, venues, places, dlr_db, dlr_cursor)
agregar_CA(address, street, venues, places, dlr_db, dlr_cursor)
agregar_Provincia(address, street, venues, places, dlr_db, dlr_cursor)
# agregar_Comarca(address, street, venues, places, dlr_db, dlr_cursor)
agregar_Municipio(address, street, venues, places, dlr_db, dlr_cursor)
agregar_Nivel(address, street, venues, places, dlr_db, dlr_cursor)
agregar_Nivel1(address, street, venues, places, dlr_db, dlr_cursor)
# agregar_Nivel2(address, street, venues, places, dlr_db, dlr_cursor)
agregar_TipoVia(address, street, venues, places, dlr_db, dlr_cursor)
agregar_Via(address, street, venues, places, dlr_db, dlr_cursor)
# agregar_ViaAntigua(address, street, venues, places, dlr_db, dlr_cursor)
agregar_Direccion(address, street, venues, places, dlr_db, dlr_cursor)
agregar_NombrePropio(address, street, venues, places, dlr_db, dlr_cursor)
agregar_CodPostal_Nivel(address, street, venues, places, dlr_db, dlr_cursor)
agregar_CodPostal_Municipio(address, street, venues, places, dlr_db, dlr_cursor)

# dlr_cursor.execute("SELECT * FROM CA")
#
# for x in dlr_cursor:
#     print(x)

dlr_db.close()
