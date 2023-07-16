import unittest
from cassandra.cluster import Cluster

class TestStringMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        global cluster
        cluster = Cluster(contact_points=['localhost',], port=9042)

        global session
        session = cluster.connect('prueba')

    def test_connection(self):
        cluster_test = Cluster(contact_points=['localhost',], port=9042)
        session_test = cluster_test.connect('prueba')
        self.assertEqual("","")

    def test_estado_ca(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.estado_ca WHERE nombreEstado = 'España'").one().nombreestado, 'España')

    def test_ca_provincia(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.ca_provincia WHERE nombreCA = 'Extremadura'").one().nombreca, 'Extremadura')

    def test_provincia_municipio(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.provincia_municipio WHERE nombreProvincia = 'Albacete'").one().nombreprovincia, 'Albacete')

    def test_municipio_nivel(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.municipio_nivel WHERE nombreMunicipio = 'Ventrosa'").one().nombremunicipio, 'Ventrosa')

    def test_nivel_via(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.nivel_via WHERE nombreNivel = 'Lagunilla del Jubera'").one().nombrenivel, 'Lagunilla del Jubera')

    def test_municipio_via(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.municipio_via WHERE nombreMunicipio = 'Brieva de Cameros'").one().nombremunicipio, 'Brieva de Cameros')

    def test_via_direccion(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.via_direccion WHERE nombreVia = 'Danzadores'").one().nombrevia, 'Danzadores')

    def test_tipovia_via(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.tipovia_via WHERE nombreTipoVia = 'Pasadizo'").one().nombretipovia, 'Pasadizo')

    def test_estado(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.estado WHERE nombreEstado = 'España'").one().nombreestado, 'España')

    def test_ca(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.ca WHERE nombreCA = 'Navarra'").one().nombreca, 'Navarra')

    def test_provincia(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.provincia WHERE nombreProvincia = 'La Rioja'").one().nombreprovincia, 'La Rioja')

    def test_municipio(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.municipio WHERE nombreMunicipio = 'Logroño'").one().nombremunicipio, 'Logroño')

    def test_nivel(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.nivel WHERE nombreNivel = 'Logroño'").one().nombrenivel, 'Logroño')

    def test_via(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.via WHERE nombreVia = 'Gran Vía del Rey Don Juan Carlos I'").one().nombrevia, 'Gran Vía del Rey Don Juan Carlos I')

    def test_codPostal(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.codPostal WHERE codPostal = '26532'").one().codpostal, '26532')

    def test_numero(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.numero WHERE numero = 339").one().numero, 339)

    def test_tipovia(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.tipovia WHERE nombreTipoVia = 'Calle'").one().nombretipovia, 'Calle')

    def test_nombrepropio(self):
        self.assertEqual(session.execute("SELECT * FROM prueba.nombrepropio WHERE nombre = 'Casa de las Ciencias'").one().nombre, 'Casa de las Ciencias')

if __name__ == '__main__':
    unittest.main()
