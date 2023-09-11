# BCP2 (TFM2) - Carga de datos
Parte del Trabajo de Fin de Máster del Máster en Ciencia de Datos y Aprendizaje Automático de la Universidad de La Rioja. Carga de datos en la BD MySQL y en las bases de datos Cassandra y Redis.

## Estructura del proyecto:
### _Datos_

Ficheros CSV de partida para la carga de datos en las BD de registros de referencia y para la georreferenciación de direcciones.

#### _Datos/T1_

Datos relativos a los registros de referencia en la Comunidad Autónoma de La Rioja, España. Fuente: [IDERioja](https://www.iderioja.larioja.org/).

#### _Datos/T2_

Datos relativos a las direcciones objetivo.

### _MySQL-noSQL_

Scripts de carga de datos a los entornos NoSQL a partir de la BD MySQL.

#### _MySQL-noSQL/Cassandra_

Scripts de creación, limpieza y carga de datos en la BD no relacional Cassandra.

#### _MySQL-noSQL/Redis_

Scripts de carga de datos en la BD no relacional Redis.

### _MySQL_

Scripts de carga de datos de la carpeta _Datos/T1_ a la BD MySQL.

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
