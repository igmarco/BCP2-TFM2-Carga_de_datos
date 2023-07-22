"""
Definimos los parámetros correspondientes a las consultas de la BD MySQL.
"""
# Definimos los parámetros de las consultas de relación jerárquica nominal-nominal.
conexiones = [
    {
        # Estado --> Comunidades Autónomas
        'nombre':'estado_ca',
        'campos':['nombreEstado', 'nombreCA'],
        'campo_id': 'nombreEstado',
        'campo_lista': 'nombreCA',
        'tablas':['estado','CA'],
        'using':['idEstado'],
        'orderby':['nombreEstado','nombreCA']
    },
    {
        # Comunidad Autónoma --> Provincias
        'nombre':'ca_provincia',
        'campos':['nombreCA', 'nombreProvincia'],
        'campo_id': 'nombreCA',
        'campo_lista': 'nombreProvincia',
        'tablas':['CA','provincia'],
        'using':['idCA'],
        'orderby':['nombreCA','nombreProvincia']
    },
    {
        # Provincia --> Comarcas
        'nombre':'provincia_comarca',
        'campos':['nombreProvincia', 'nombreComarca'],
        'campo_id': 'nombreProvincia',
        'campo_lista': 'nombreComarca',
        'tablas':['provincia','comarca'],
        'using':['idProvincia'],
        'orderby':['nombreProvincia','nombreComarca']
    },
    {
        # Comarca --> Municipios
        'nombre':'comarca_municipio',
        'campos':['nombreComarca', 'nombreMunicipio'],
        'campo_id': 'nombreComarca',
        'campo_lista': 'nombreMunicipio',
        'tablas':['comarca','municipio'],
        'using':['idComarca'],
        'orderby':['nombreComarca','nombreMunicipio']
    },
    {
        # Provincia --> Municipios
        'nombre':'provincia_municipio',
        'campos':['nombreProvincia', 'nombreMunicipio'],
        'campo_id': 'nombreProvincia',
        'campo_lista': 'nombreMunicipio',
        'tablas':['provincia','municipio'],
        'using':['idProvincia'],
        'orderby':['nombreProvincia','nombreMunicipio']
    },
    {
        # Municipio --> Nivel1s
        'nombre':'municipio_nivel',
        'campos':['nombreMunicipio', 'nombreNivel'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'nombreNivel',
        'tablas':['municipio','nivel1', 'nivel'],
        'using':['idMunicipio', 'idNivel'],
        'orderby':['nombreMunicipio','nombreNivel']
    },
    {
        # Municipio --> Nivel2s
        'nombre':'municipio_nivel',
        'campos':['nombreMunicipio', 'nombreNivel'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'nombreNivel',
        'tablas':['municipio','nivel1', 'nivel2', 'nivel'],
        'using':['idMunicipio', 'idNivel1', 'idNivel'],
        'orderby':['nombreMunicipio','nombreNivel']
    },
    {
        # Nivel1 --> Vías
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'nombreVia'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'nombreVia',
        'tablas':['nivel', 'nivel1', 'via'],
        'using':['idNivel', 'idNivel1'],
        'orderby':['nombreNivel','nombreVia']
    },
    {
        # Nivel2 --> Vías
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'nombreVia'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'nombreVia',
        'tablas':['nivel', 'nivel2', 'via'],
        'using':['idNivel', 'idNivel2'],
        'orderby':['nombreNivel','nombreVia']
    },
    {
        # Nivel1 --> Vías antiguas
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'viaantigua.nombreVia'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'viaantigua.nombreVia',
        'tablas':['nivel', 'nivel1', 'via', 'viaantigua'],
        'using':['idNivel', 'idNivel1', 'idVia'],
        'orderby':['nombreNivel','nombreVia']
    },
    {
        # Nivel2 --> Vías antiguas
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'viaantigua.nombreVia'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'viaantigua.nombreVia',
        'tablas':['nivel', 'nivel2', 'via', 'viaantigua'],
        'using':['idNivel', 'idNivel2', 'idVia'],
        'orderby':['nombreNivel','nombreVia']
    },
    {
        # Municipio --> Vías
        'nombre':'municipio_via',
        'campos':['nombreMunicipio', 'nombreVia'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'nombreVia',
        'tablas':['municipio','via'],
        'using':['idMunicipio'],
        'orderby':['nombreMunicipio','nombreVia']
    },
    {
        # Municipio --> Vías antiguas
        'nombre':'municipio_via',
        'campos':['nombreMunicipio', 'viaantigua.nombreVia'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'viaantigua.nombreVia',
        'tablas':['municipio','via', 'viaantigua'],
        'using':['idMunicipio', 'idVia'],
        'orderby':['nombreMunicipio','viaantigua.nombreVia']
    },
    {
        # Tipo de vía --> Vías
        'nombre':'tipovia_via',
        'campos':['nombreTipoVia', 'nombreVia'],
        'campo_id': 'nombreTipoVia',
        'campo_lista': 'nombreVia',
        'tablas':['tipoVia', 'via'],
        'using':['idTipoVia'],
        'orderby':['nombreTipoVia','nombreVia']
    },
    {
        # Tipo de vía --> Vías antiguas
        'nombre':'tipovia_via',
        'campos':['nombreTipoVia', 'nombreVia'],
        'campo_id': 'nombreTipoVia',
        'campo_lista': 'nombreVia',
        'tablas':['tipoVia', 'viaantigua'],
        'using':['idTipoVia'],
        'orderby':['nombreTipoVia','nombreVia']
    },
    {
        # Vía --> Códigos Postales
        'nombre':'via_codPostal',
        'campos':['nombreVia', 'codPostal'],
        'campo_id': 'nombreVia',
        'campo_lista': 'codPostal',
        'tablas':['via', 'direccion'],
        'using':['idVia'],
        'orderby':['nombreVia','codPostal']
    },
    {
        # Vía --> Números
        'nombre':'via_numero',
        'campos':['nombreVia', 'numero'],
        'campo_id': 'nombreVia',
        'campo_lista': 'numero',
        'tablas':['via', 'direccion'],
        'using':['idVia'],
        'orderby':['nombreVia','numero']
    },
    {
        # Vía antigua --> Códigos Postales
        'nombre':'via_codPostal',
        'campos':['nombreVia', 'codPostal'],
        'campo_id': 'nombreVia',
        'campo_lista': 'codPostal',
        'tablas':['viaantigua', 'direccion'],
        'using':['idVia'],
        'orderby':['nombreVia','codPostal']
    },
    {
        # Vía antigua --> Números
        'nombre':'via_numero',
        'campos':['nombreVia', 'numero'],
        'campo_id': 'nombreVia',
        'campo_lista': 'numero',
        'tablas':['viaantigua', 'direccion'],
        'using':['idVia'],
        'orderby':['nombreVia','numero']
    },
]

# Definimos los parámetros de las consultas de relación jerárquica nominal-estricta.
dependencias = [
    {
        # Estado --> Comunidades Autónomas
        'nombre':'estado_ca',
        'campos':['nombreEstado', 'nombreCA', 'idCA'],
        'campo_id': 'nombreEstado',
        'campo_lista': 'idCA',
        'tablas':['estado','CA'],
        'using':['idEstado'],
        'orderby':['nombreEstado','idCA']
    },
    {
        # Comunidad Autónoma --> Provincias
        'nombre':'ca_provincia',
        'campos':['nombreCA', 'nombreProvincia', 'idProvincia'],
        'campo_id': 'nombreCA',
        'campo_lista': 'idProvincia',
        'tablas':['CA','provincia'],
        'using':['idCA'],
        'orderby':['nombreCA','idProvincia']
    },
    {
        # Provincia --> Comarcas
        'nombre':'provincia_comarca',
        'campos':['nombreProvincia', 'nombreComarca', 'idComarca', 'tipoComarca'],
        'campo_id': 'nombreProvincia',
        'campo_lista': 'idComarca',
        'tablas':['provincia','comarca'],
        'using':['idProvincia'],
        'orderby':['nombreProvincia','idComarca']
    },
    {
        # Comarca --> Municipios
        'nombre':'comarca_municipio',
        'campos':['nombreComarca', 'nombreMunicipio', 'idMunicipio'],
        'campo_id': 'nombreComarca',
        'campo_lista': 'idMunicipio',
        'tablas':['comarca','municipio'],
        'using':['idComarca'],
        'orderby':['nombreComarca','idMunicipio']
    },
    {
        # Provincia --> Municipios
        'nombre':'provincia_municipio',
        'campos':['nombreProvincia', 'nombreMunicipio', 'idMunicipio'],
        'campo_id': 'nombreProvincia',
        'campo_lista': 'idMunicipio',
        'tablas':['provincia','municipio'],
        'using':['idProvincia'],
        'orderby':['nombreProvincia','idMunicipio']
    },
    {
        # Municipio --> Nivel1s
        'nombre':'municipio_nivel',
        'campos':['nombreMunicipio', 'nombreNivel', 'idNivel', 'tipoNivel'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'idNivel',
        'tablas':['municipio','nivel1', 'nivel'],
        'using':['idMunicipio', 'idNivel'],
        'orderby':['nombreMunicipio','idNivel']
    },
    {
        # Municipio --> Nivel2s
        'nombre':'municipio_nivel',
        'campos':['nombreMunicipio', 'nombreNivel', 'idNivel', 'tipoNivel'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'idNivel',
        'tablas':['municipio','nivel1', 'nivel2', 'nivel'],
        'using':['idMunicipio', 'idNivel1', 'idNivel'],
        'orderby':['nombreMunicipio','idNivel']
    },
    {
        # Nivel1 --> Vías
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'nombreVia', 'idVia', 'idTipoVia', 'nombreTipoVia', 'detalle'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'idVia',
        'tablas':['nivel', 'nivel1', 'via', 'tipoVia'],
        'using':['idNivel', 'idNivel1', 'idTipoVia'],
        'orderby':['nombreNivel','idVia']
    },
    {
        # Nivel2 --> Vías
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'nombreVia', 'idVia', 'idTipoVia', 'nombreTipoVia', 'detalle'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'idVia',
        'tablas':['nivel', 'nivel2', 'via', 'tipoVia'],
        'using':['idNivel', 'idNivel2', 'idTipoVia'],
        'orderby':['nombreNivel','idVia']
    },
    {
        # Nivel1 --> Vías antiguas
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'viaantigua.nombreVia', 'viaantigua.idVia', 'viaantigua.idTipoVia', 'nombreTipoVia', 'viaantigua.detalle'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'idVia',
        'tablas':['nivel', 'nivel1', 'via', 'viaantigua', 'tipoVia'],
        'using':['idNivel', 'idNivel1', 'idVia', 'idTipoVia'],
        'orderby':['nombreNivel','idVia']
    },
    {
        # Nivel2 --> Vías antiguas
        'nombre':'nivel_via',
        'campos':['nombreNivel', 'viaantigua.nombreVia', 'viaantigua.idVia', 'viaantigua.idTipoVia', 'nombreTipoVia', 'viaantigua.detalle'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'idVia',
        'tablas':['nivel', 'nivel2', 'via', 'viaantigua', 'tipoVia'],
        'using':['idNivel', 'idNivel2', 'idVia', 'idTipoVia'],
        'orderby':['nombreNivel','idVia']
    },
    {
        # Municipio --> Vías
        'nombre':'municipio_via',
        'campos':['nombreMunicipio', 'nombreVia', 'idVia', 'idTipoVia', 'nombreTipoVia', 'detalle'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'idVia',
        'tablas':['municipio','via', 'tipoVia'],
        'using':['idMunicipio', 'idTipoVia'],
        'orderby':['nombreMunicipio','idVia']
    },
    {
        # Municipio --> Vías antiguas
        'nombre':'municipio_via',
        'campos':['nombreMunicipio', 'viaantigua.nombreVia', 'viaantigua.idVia', 'viaantigua.idTipoVia', 'nombreTipoVia', 'viaantigua.detalle'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'idVia',
        'tablas':['municipio','via', 'viaantigua', 'tipoVia'],
        'using':['idMunicipio', 'idVia', 'idTipoVia'],
        'orderby':['nombreMunicipio','viaantigua.idVia']
    },
    {
        # Tipo de vía --> Vías
        'nombre':'tipovia_via',
        'campos':['nombreTipoVia', 'nombreVia', 'idVia', 'idTipoVia', 'detalle'],
        'campo_id': 'nombreTipoVia',
        'campo_lista': 'idVia',
        'tablas':['tipoVia', 'via'],
        'using':['idTipoVia'],
        'orderby':['nombreTipoVia','idVia']
    },
    {
        # Tipo de vía --> Vías antiguas
        'nombre':'tipovia_via',
        'campos':['nombreTipoVia', 'nombreVia', 'idVia', 'idTipoVia', 'detalle'],
        'campo_id': 'nombreTipoVia',
        'campo_lista': 'idVia',
        'tablas':['tipoVia', 'viaantigua'],
        'using':['idTipoVia'],
        'orderby':['nombreTipoVia','idVia']
    },
    {
        # Vía --> Direcciones
        'nombre':'via_direccion',
        'campos':['nombreVia', 'codPostal', 'numero', 'idDireccion', 'direccion.detalle', 'nombre'],
        'campo_id': 'nombreVia',
        'campo_lista': 'idDireccion',
        'tablas':['via', 'direccion', 'nombrepropio'],
        'using':['idVia', 'idDireccion'],
        'orderby':['nombreVia','idDireccion']
    },
    {
        # Vía antigua --> Direcciones
        'nombre':'via_direccion',
        'campos':['nombreVia', 'codPostal', 'numero', 'idDireccion', 'direccion.detalle', 'nombre'],
        'campo_id': 'nombreVia',
        'campo_lista': 'idDireccion',
        'tablas':['viaantigua', 'direccion', 'nombrepropio'],
        'using':['idVia', 'idDireccion'],
        'orderby':['nombreVia','idDireccion']
    },
]

# Definimos los parámetros de las consultas de entidad jerárquica.
selecciones = [
    {
        # Estado (Nombre) --> Estados (ID)
        'nombre':'estado',
        'campos':['idEstado', 'nombreEstado'],
        'campo_id': 'nombreEstado',
        'campo_lista': 'idEstado',
        'tablas':['estado'],
        'using':[],
        'orderby':['nombreEstado']
    },
    {
        # Comunidad Autónoma (Nombre) --> Comunidades Autónomas (ID)
        'nombre':'ca',
        'campos':['idCA', 'nombreCA', 'idEstado'],
        'campo_id': 'nombreCA',
        'campo_lista': 'idCA',
        'tablas':['ca'],
        'using':[],
        'orderby':['nombreCA']
    },
    {
        # Provincia (Nombre) --> Provincias (ID)
        'nombre':'provincia',
        'campos':['idProvincia', 'nombreProvincia', 'idCA'],
        'campo_id': 'nombreProvincia',
        'campo_lista': 'idProvincia',
        'tablas':['provincia'],
        'using':[],
        'orderby':['nombreProvincia']
    },
    {
        # Comarca (Nombre) --> Comarcas (ID)
        'nombre':'comarca',
        'campos':['idComarca', 'nombreComarca', 'tipoComarca', 'idProvincia'],
        'campo_id': 'nombreComarca',
        'campo_lista': 'idComarca',
        'tablas':['comarca'],
        'using':[],
        'orderby':['nombreComarca']
    },
    {
        # Municipio (Nombre) --> Municipios (ID)
        'nombre':'municipio',
        'campos':['idMunicipio', 'nombreMunicipio', 'idProvincia', 'idComarca'],
        'campo_id': 'nombreMunicipio',
        'campo_lista': 'idMunicipio',
        'tablas':['municipio'],
        'using':[],
        'orderby':['nombreMunicipio']
    },
    {
        # Nivel1 (Nombre) --> Nivel1s (ID)
        'nombre':'nivel',
        'campos':['idNivel', 'nombreNivel', 'tipoNivel', 'idMunicipio', 'idNivel1'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'idNivel',
        'tablas':['nivel', 'nivel1'],
        'using':['idNivel'],
        'orderby':['nombreNivel']
    },
    {
        # Nivel2 (Nombre) --> Nivel2s (ID)
        'nombre':'nivel',
        'campos':['idNivel', 'nombreNivel', 'tipoNivel', 'idNivel1', 'idNivel2'],
        'campo_id': 'nombreNivel',
        'campo_lista': 'idNivel',
        'tablas':['nivel', 'nivel2'],
        'using':['idNivel'],
        'orderby':['nombreNivel']
    },
    {
        # Vía (Nombre) --> Vías (ID)
        'nombre':'via',
        'campos':['idVia', 'nombreVia', 'idTipoVia', 'nombreTipoVia', 'detalle', 'idMunicipio', 'idNivel1', 'idNivel2'],
        'campo_id': 'nombreVia',
        'campo_lista': 'idVia',
        'tablas':['via', 'tipoVia'],
        'using':['idTipoVia'],
        'orderby':['nombreVia']
    },
    {
        # Vía (Nombre) --> Vías antiguas (ID)
        'nombre':'viaantigua',
        'campos':['idVia', 'idViaAntigua', 'nombreVia', 'idTipoVia', 'nombreTipoVia', 'detalle'],
        'campo_id': 'nombreVia',
        'campo_lista': 'idVia',
        'tablas':['viaantigua', 'tipoVia'],
        'using':['idTipoVia'],
        'orderby':['nombreVia']
    },
    {
        # Código Postal (Nombre) --> Direcciones (ID)
        'nombre':'codPostal',
        'campos':['idDireccion', 'idVia', 'codPostal', 'numero', 'detalle', 'nombre'],
        'campo_id': 'codPostal',
        'campo_lista': 'numero',
        'tablas':['direccion', 'nombrepropio'],
        'using':['idDireccion'],
        'orderby':['codPostal']
    },
    {
        # Número (Nombre) --> Direcciones (ID)
        'nombre':'numero',
        'campos':['idDireccion', 'idVia', 'codPostal', 'numero', 'detalle', 'nombre'],
        'campo_id': 'numero',
        'campo_lista': 'codPostal',
        'tablas':['direccion', 'nombrepropio'],
        'using':['idDireccion'],
        'orderby':['numero']
    },
    {
        # Tipo de vía (Nombre) --> Tipos de vía (ID)
        'nombre':'tipovia',
        'campos':['idTipoVia', 'nombreTipoVia'],
        'campo_id': 'nombreTipoVia',
        'campo_lista': 'idTipoVia',
        'tablas':['tipovia'],
        'using':[],
        'orderby':['nombreTipoVia']
    },
    {
        # Nombre propio (Nombre) --> Direcciones (ID)
        'nombre':'nombrepropio',
        'campos':['idDireccion', 'nombre', 'numero', 'codPostal', 'nombrevia', 'nombremunicipio',
                  'nombreprovincia', 'nombreca', 'nombreestado'],
        'campo_id': 'nombre',
        'campo_lista': 'idDireccion',
        'tablas':['nombrepropio', 'direccion', 'via', 'municipio', 'provincia', 'ca', 'estado'],
        'using':['idDireccion', 'idVia', 'idMunicipio', 'idProvincia', 'idCA', 'idEstado'],
        'orderby':['nombre']
    },
]