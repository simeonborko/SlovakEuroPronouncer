from unittest import TestCase
from decimal import Decimal
from .SlovakEuroPronouncer import pronounce, pronounce_with_cents


class TestPronouncer(TestCase):

    def test_fail(self):
        self.assertRaises(Exception, pronounce, -1)
        self.assertRaises(Exception, pronounce, 1000000)

    def test_1(self):
        self.assertEqual('nula eur', pronounce(0))

        self.assertEqual('deväť eur', pronounce(9))
        self.assertEqual('štyri eurá', pronounce(4))

    def test_2(self):
        self.assertEqual('štrnásť eur', pronounce(14))
        self.assertEqual('sedemdesiatosem eur', pronounce(78))
        self.assertEqual('päťdesiat eur', pronounce(50))
        self.assertEqual('desať eur', pronounce(10))
        self.assertEqual('devätnásť eur', pronounce(19))

    def test_3(self):
        self.assertEqual('sto eur', pronounce(100))
        self.assertEqual('dvestotridsaťdva eur', pronounce(232))
        self.assertEqual('tristotridsať eur', pronounce(330))
        self.assertEqual('šesťstojeden eur', pronounce(601))
        self.assertEqual('deväťstodeväťdesiat eur', pronounce(990))
        self.assertEqual('sedemstosedemdesiatsedem eur', pronounce(777))

    def test_4(self):
        self.assertEqual('tisíc eur', pronounce(1000))
        self.assertEqual('tisícstojeden eur', pronounce(1101))
        self.assertEqual('dvetisíctristopäťdesiat eur', pronounce(2350))
        self.assertEqual('päťtisícpäťstoštyridsaťštyri eur', pronounce(5544))
        self.assertEqual('sedemtisícsedemdesiat eur', pronounce(7070))
        self.assertEqual('dvetisícdvesto eur', pronounce(2200))

    def test_5(self):
        self.assertEqual('desaťtisíc eur', pronounce(10000))
        self.assertEqual('dvadsaťdvatisíc eur', pronounce(22000))
        self.assertEqual('tridsaťtritisíctri eur', pronounce(33003))
        self.assertEqual('päťdesiattisícpäťstopäť eur', pronounce(50505))
        self.assertEqual('päťdesiattisícpäťdesiat eur', pronounce(50050))
        self.assertEqual('pätnásťtisícdvestodvadsať eur', pronounce(15220))
        self.assertEqual('sedemdesiatosemtisíctridsaťpäť eur', pronounce(78035))

    def test_6(self):
        self.assertEqual('stotisíc eur', pronounce(100000))
        self.assertEqual('stotridsaťtritisícdva eur', pronounce(133002))
        self.assertEqual('sedemstotisícsto eur', pronounce(700100))
        self.assertEqual('dvestodvadsaťtisícdva eur', pronounce(220002))
        self.assertEqual('tristotisíctristotri eur', pronounce(300303))

    def test_7(self):
        self.assertEqual('stodvadsaťtri eur a 1 cent', pronounce_with_cents(Decimal('123.01')))
        self.assertEqual('stodvadsaťtri eur a 2 centy', pronounce_with_cents(Decimal('123.02')))
        self.assertEqual('stodvadsaťtri eur a 45 centov', pronounce_with_cents(Decimal('123.45')))
