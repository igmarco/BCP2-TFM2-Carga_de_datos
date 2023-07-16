import mysql.connector
from cassandra.cluster import Cluster

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

# Conectamos con la BD Cassandra
cluster = Cluster(contact_points=['localhost',], port=9042)
session = cluster.connect('prueba')

# Cargamos las dependencias
for dependencia in infoConsultas_carga_datosT1_noSQL.dependencias:
    sql = funciones_carga_datosT1_noSQL.construccion_sqlquery(dependencia)

    mycursor.execute(sql)

    funciones_carga_datosT1_noSQL.carga_cassandra_compacta(dependencia, mycursor, session)

    print('Se ha cargado un paquete de dependencia:', dependencia['nombre'])
    print()

# Cargamos las selecciones
for seleccion in infoConsultas_carga_datosT1_noSQL.selecciones:
    sql = funciones_carga_datosT1_noSQL.construccion_sqlquery(seleccion)

    mycursor.execute(sql)

    funciones_carga_datosT1_noSQL.carga_cassandra_compacta(seleccion, mycursor, session)

    print('Se ha cargado un paquete de selección:', seleccion['nombre'])
    print()