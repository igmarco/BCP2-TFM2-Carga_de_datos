DROP DATABASE DIRECCIONES_LARIOJA;
CREATE DATABASE DIRECCIONES_LARIOJA;

SHOW DATABASES;
USE DIRECCIONES_LARIOJA;

SHOW TABLES;
CREATE TABLE Estado (
    idEstado 		varchar(255)	PRIMARY KEY,
    nombreEstado 	varchar(255)	NOT NULL
);

SHOW TABLES;
CREATE TABLE CA (
    idCA 			varchar(255)	PRIMARY KEY,
    nombreCA 		varchar(255)	NOT NULL,
    idEstado		varchar(255)	NOT NULL,
    FOREIGN KEY (idEstado) REFERENCES Estado (idEstado)
);

SHOW TABLES;
CREATE TABLE Provincia (
    idProvincia 	varchar(255)	PRIMARY KEY,
    nombreProvincia varchar(255)	NOT NULL,
    idCA			varchar(255)	NOT NULL,
    FOREIGN KEY (idCA) REFERENCES CA (idCA)
);

SHOW TABLES;
CREATE TABLE Comarca (
    idComarca 		varchar(255)	PRIMARY KEY,
    nombreComarca 	varchar(255)	NOT NULL,
    tipoComarca		varchar(255)	NOT NULL,
    idProvincia		varchar(255)	NOT NULL,
    FOREIGN KEY (idProvincia) REFERENCES Provincia (idProvincia)
);

SHOW TABLES;
CREATE TABLE Municipio (
    idMunicipio 	varchar(255)	PRIMARY KEY,
    nombreMunicipio varchar(255)	NOT NULL,
    idProvincia		varchar(255)	NOT NULL,
    idComarca		varchar(255),
    FOREIGN KEY (idComarca) REFERENCES Comarca (idComarca),
    FOREIGN KEY (idProvincia) REFERENCES Provincia (idProvincia)
);

SHOW TABLES;
CREATE TABLE Nivel (
    idNivel 		varchar(255)	PRIMARY KEY,
    nombreNivel 	varchar(255)	NOT NULL,
    tipoNivel		varchar(255)	NOT NULL
);

SHOW TABLES;
CREATE TABLE Nivel1 (
    idNivel1 		varchar(255)	PRIMARY KEY,
    idNivel			varchar(255)	NOT NULL,
    idMunicipio		varchar(255)	NOT NULL,
    FOREIGN KEY (idNivel) REFERENCES Nivel (idNivel),
    FOREIGN KEY (idMunicipio) REFERENCES Municipio (idMunicipio)
);

SHOW TABLES;
CREATE TABLE Nivel2 (
    idNivel2 		varchar(255)	PRIMARY KEY,
    idNivel			varchar(255)	NOT NULL,
    idNivel1		varchar(255)	NOT NULL,
    FOREIGN KEY (idNivel) REFERENCES Nivel (idNivel),
    FOREIGN KEY (idNivel1) REFERENCES Nivel1 (idNivel1)
);

SHOW TABLES;
CREATE TABLE TipoVia (
    idTipoVia 		int				PRIMARY KEY,
    nombreTipoVia 	varchar(255)	NOT NULL
);

SHOW TABLES;
CREATE TABLE Via (
    idVia 			varchar(255)	PRIMARY KEY,
    idMunicipio		varchar(255)	NOT NULL,
    idNivel1		varchar(255),
    idNivel2		varchar(255),
    idTipoVia		int				NOT NULL,
    nombreVia		varchar(255)	NOT NULL,
    detalle			varchar(255),
--     longitud		float			NOT NULL,
--     latitud		float			NOT NULL,
	posicion		point			NOT NULL,
    SPATIAL KEY posicion (posicion),
    FOREIGN KEY (idMunicipio) REFERENCES Municipio (idMunicipio),
    FOREIGN KEY (idNivel1) REFERENCES Nivel1 (idNivel1),
    FOREIGN KEY (idNivel2) REFERENCES Nivel2 (idNivel2),
    FOREIGN KEY (idTipoVia) REFERENCES TipoVia (idTipoVia)-- ,
--     CONSTRAINT unq_lonlat_V UNIQUE (longitud, latitud)
);

SHOW TABLES;
CREATE TABLE ViaAntigua (
	idViaAntigua	int				NOT NULL,
	idVia			varchar(255)	NOT NULL,
    idTipoVia		int				NOT NULL,
    nombreVia		varchar(255)	NOT NULL,
    detalle			varchar(255),
    PRIMARY KEY (idViaAntigua, idVia),
    FOREIGN KEY (idVia) REFERENCES Via (idVia),
    FOREIGN KEY (idTipoVia) REFERENCES TipoVia (idTipoVia)
);

SHOW TABLES;
CREATE TABLE Direccion (
    idDireccion 	varchar(255)	PRIMARY KEY,
    idVia			varchar(255)	NOT NULL,
    codPostal		CHAR(5)			NOT NULL,
    numero			int,
    detalle			varchar(255),
--     longitud		float			NOT NULL,
--     latitud		float			NOT NULL,
	posicion		point			NOT NULL,
    SPATIAL KEY posicion (posicion),
--     CONSTRAINT unq_lonlat_D UNIQUE (longitud, latitud),
    FOREIGN KEY (idVia) REFERENCES Via (idVia)-- ,
--     CONSTRAINT chk_codPostal_Direccion CHECK (codPostal like '[0-9][0-9][0-9][0-9][0-9]')
);

SHOW TABLES;
CREATE TABLE NombrePropio (
    idDireccion		varchar(255)	NOT NULL,
    nombre 			varchar(255)	NOT NULL,
    PRIMARY KEY (idDireccion, nombre),
    FOREIGN KEY (idDireccion) REFERENCES Direccion (idDireccion)
);

SHOW TABLES;
CREATE TABLE CodPostal_Municipio (
    codPostal 		char(5)			NOT NULL,
    idMunicipio		varchar(255)	NOT NULL,
    PRIMARY KEY (codPostal, idMunicipio),
    FOREIGN KEY (idMunicipio) REFERENCES Municipio (idMunicipio)-- ,
--     CONSTRAINT chk_codPostal_Municipio CHECK (codPostal like '[0-9][0-9][0-9][0-9][0-9]')
);

SHOW TABLES;
CREATE TABLE CodPostal_Nivel (
    codPostal 		char(5)			NOT NULL,
    idNivel			varchar(255)	NOT NULL,
    PRIMARY KEY (codPostal, idNivel),
    FOREIGN KEY (idNivel) REFERENCES Nivel (idNivel)-- ,
--     CONSTRAINT chk_codPostal_Nivel CHECK (codPostal like '[0-9][0-9][0-9][0-9][0-9]')
);

SHOW TABLES;
