import mysql.connector
import redis

import sys
sys.path.append('..')

import funciones_carga_datosT1_noSQL
import infoConsultas_carga_datosT1_noSQL

# Conectamos con la BD MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="direcciones_larioja"
)

mycursor = mydb.cursor(buffered=True, dictionary=True)

# Conectamos con la BD Redis
r = redis.StrictRedis(host='localhost', port=6379, db=11)

# Ejecutamos el reseteo de la BD 11
r.flushdb()

# Cargamos las conexiones
for conexion in infoConsultas_carga_datosT1_noSQL.conexiones:
    sql = funciones_carga_datosT1_noSQL.construccion_sqlquery(conexion)

    mycursor.execute(sql)

    subregions = funciones_carga_datosT1_noSQL.construccion_subregions(conexion, mycursor)

    for region in subregions:
        funciones_carga_datosT1_noSQL.carga_subregions_redis(conexion, region, subregions[region], r)

    print('Se ha cargado un paquete de conexión:', conexion['nombre'])
    print()

# Cargamos las selecciones
for seleccion in infoConsultas_carga_datosT1_noSQL.selecciones:
    sql = funciones_carga_datosT1_noSQL.construccion_sqlquery(seleccion)

    mycursor.execute(sql)

    subregions = funciones_carga_datosT1_noSQL.construccion_regions(seleccion, mycursor)

    for region in subregions:
        funciones_carga_datosT1_noSQL.carga_regions_redis(seleccion, region, subregions[region], r)

    print('Se ha cargado un paquete de selección:', seleccion['nombre'])
    print()