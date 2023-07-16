CREATE TABLE estado_ca(
	nombreEstado varchar,
	nombreCA varchar,
	idCA varchar,
	PRIMARY KEY (nombreEstado, idCA)
);

CREATE TABLE ca_provincia(
	nombreCA varchar,
	nombreProvincia varchar,
	idProvincia varchar,
	PRIMARY KEY (nombreCA, idProvincia)
);

CREATE TABLE provincia_comarca(
	nombreProvincia varchar,
	nombreComarca varchar,
	idComarca varchar,
	tipoComarca varchar,
	PRIMARY KEY (nombreProvincia, idComarca)
);

CREATE TABLE comarca_municipio(
	nombreComarca varchar,
	nombreMunicipio varchar,
	idMunicipio varchar,
	PRIMARY KEY (nombreComarca, idMunicipio)
);

CREATE TABLE provincia_municipio(
	nombreProvincia varchar,
	nombreMunicipio varchar,
	idMunicipio varchar,
	PRIMARY KEY (nombreProvincia, idMunicipio)
);

CREATE TABLE municipio_nivel(
	nombreMunicipio varchar,
	nombreNivel varchar,
	idNivel varchar,
	tipoNivel varchar,
	PRIMARY KEY (nombreMunicipio, idNivel)
);

CREATE TABLE nivel_via(
	nombreNivel varchar,
	nombreVia varchar,
	idVia varchar,
	idTipoVia int,
	nombreTipoVia varchar,
	detalle varchar,
	PRIMARY KEY (nombreNivel, idVia)
);

CREATE TABLE municipio_via(
	nombreMunicipio varchar,
	nombreVia varchar,
	idVia varchar,
	idTipoVia int,
	nombreTipoVia varchar,
	detalle varchar,
	PRIMARY KEY (nombreMunicipio, idVia)
);

CREATE TABLE tipovia_via(
	nombreTipoVia varchar,
	nombreVia varchar,
	idVia varchar,
	idTipoVia int,
	detalle varchar,
	PRIMARY KEY (nombreTipoVia, idVia)
);

CREATE TABLE via_direccion(
	nombreVia varchar,
	codPostal varchar,
	numero int,
	idDireccion varchar,
	detalle varchar,
	nombre varchar,
	PRIMARY KEY (nombreVia, idDireccion)
);

CREATE TABLE estado(
	nombreEstado varchar,
	idEstado varchar,
	PRIMARY KEY (nombreEstado, idEstado)
);

CREATE TABLE ca(
	nombreCA varchar,
	idCA varchar,
	idEstado varchar,
	PRIMARY KEY (nombreCA, idCA)
);

CREATE TABLE provincia(
	nombreProvincia varchar,
	idProvincia varchar,
	idCA varchar,
	PRIMARY KEY (nombreProvincia, idProvincia)
);

CREATE TABLE comarca(
	nombreComarca varchar,
	idComarca varchar,
	tipoComarca varchar,
	idProvincia varchar,
	PRIMARY KEY (nombreComarca, idComarca)
);

CREATE TABLE municipio(
	nombreMunicipio varchar,
	idMunicipio varchar,
	idProvincia varchar,
	idComarca varchar,
	PRIMARY KEY (nombreMunicipio, idMunicipio)
);

CREATE TABLE nivel(
	nombreNivel varchar,
	idNivel varchar,
	tipoNivel varchar,
	idMunicipio varchar,
	idNivel1 varchar,
	idNivel2 varchar,
	PRIMARY KEY (nombreNivel, idNivel)
);

CREATE TABLE via(
	nombreVia varchar,
	idVia varchar,
	idTipoVia int,
	nombreTipoVia varchar,
	detalle varchar,
	idMunicipio varchar,
	idNivel1 varchar,
	idNivel2 varchar,
	PRIMARY KEY (nombreVia, idVia)
);

CREATE TABLE codPostal(
	codPostal varchar,
	idVia varchar,
	numero int,
	idDireccion varchar,
	detalle varchar,
	nombre varchar,
	PRIMARY KEY (codPostal, idVia, numero)
);

CREATE TABLE numero(
	numero int,
	idVia varchar,
	codPostal varchar,
	idDireccion varchar,
	detalle varchar,
	nombre varchar,
	PRIMARY KEY (numero, idVia, codPostal)
);

CREATE TABLE tipovia(
	nombreTipoVia varchar,
	idTipoVia int,
	PRIMARY KEY (nombreTipoVia, idTipoVia)
);

CREATE TABLE nombrepropio(
	nombre varchar,
	idDireccion varchar,
	PRIMARY KEY (nombre, idDireccion)
);

