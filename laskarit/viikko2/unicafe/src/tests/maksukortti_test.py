import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_lisaantyy(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 11.00 euroa")

    def test_saldo_ei_riita(self):
        kortti=Maksukortti(100)
        kortti.ota_rahaa(200)
        self.assertEqual(str(kortti),"Kortilla on rahaa 1.00 euroa")

    def test_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

    