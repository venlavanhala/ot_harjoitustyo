import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.paate = Kassapaate()
        self.paate.kassassa_rahaa = 100000
        self.paate.edulliset = 0
        self.paate.maukkaat = 0

    def test_maarat_oikein(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_edullinen_kateinen_toimii(self):
        self.paate.syo_edullisesti_kateisella(340)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)
        self.assertEqual(self.paate.edulliset, 1)
        self.assertEqual(self.paate.syo_edullisesti_kateisella(340), 100)

    def test_maukas_kateinen_toimii(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)
        self.assertEqual(self.paate.maukkaat, 1)
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(500),100)

    def test_edullinen_kateinen_ei_riita(self):
        self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.syo_edullisesti_kateisella(200), 200)

    def test_maukas_kateinen_ei_riita(self):
        self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.maukkaat, 0)
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(200), 200)

    def test_edullinen_kortti_toimii(self):
        kortti=Maksukortti(1000)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(self.paate.edulliset, 1)

    def test_maukas_kortti_toimii(self):
        kortti=Maksukortti(1000)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_edullinen_kortti_ei_riita(self):
        kortti=Maksukortti(200)
        self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.paate.edulliset, 0)

    def test_maukas_kortti_ei_riita(self):
        kortti=Maksukortti(200)
        self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_rahasampo_kasvaa(self):
        kortti=Maksukortti(0)
        self.paate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100100)

    def test_rahan_lataus(self):
        kortti=Maksukortti(0)
        self.paate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)