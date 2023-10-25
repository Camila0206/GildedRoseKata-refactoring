# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):

#Valida disminución de valor de fecha(sell_in)
    def test_sell_in_decreases_by_one_every_day(self):
        item = Item(name= "+5 Dexterity Vest", sell_in=10, quality=20)
        gildedRose = GildedRose([item])
        days = 3
        for _ in range(days):
            gildedRose.update_quality()
        self.assertEqual(7, item.sell_in)

#Valida disminución de calidad(quality) 
    def test_quality_decreases_for_normal_item(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        gildedRose = GildedRose([item])
        days = 3
        for _ in range(days):
            gildedRose.update_quality()
        self.assertEqual(17, item.quality)

#Valida que se decremente en 2 la calidad cuando el valor de vencimiento llega a su fin (sell_in=0)
    def test_quality_decreases_twice_as_fast_after_sell_in(self):
        item = Item(name="+5 Dexterity Vest", sell_in=0, quality=10)
        gildedRose = GildedRose([item])   
        gildedRose.update_quality()
        self.assertEqual(8, item.quality)
        gildedRose.update_quality()
        self.assertEqual(6, item.quality)

#Valida que la calidad de un artículo nunca es negativa 
    def test_quality_of_item_never_negative(self):
        item = Item(name="Elixir of the Mongoose", sell_in=5, quality=7)
        gilded_rose = GildedRose([item])
        days = 12
        for _ in range(days):
          gilded_rose.update_quality()
        self.assertEqual(0, item.quality)

#Valida que cuando el articulo tiene el nombre de “Aged Brie”, la calidad aumenta en 1 unidad
    def test_aged_brie_quality_increases(self):
        item = Item(name="Aged Brie", sell_in=2, quality=0)
        gilded_rose = GildedRose([item])
        days = 2
        for _ in range(days):
          gilded_rose.update_quality()
        self.assertEqual(2, item.quality)
    
if __name__ == '__main__':
     unittest.main()