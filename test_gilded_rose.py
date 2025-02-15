# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # BACKSTAGE PASSES
    def test_backstage_passes_quality_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

    def test_backstage_passes_quality_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_backstage_passes_quality_never_passed_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)         

    def test_backstage_passes_quality_never_exceeds_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in) 

    def test_backstage_passes_increases_by_2_when_sell_in_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(9, items[0].sell_in) 

    # CONJURED ITEMS
    def test_conjured_item_decreases_quality(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(2, items[0].sell_in)


    def test_conjured_cannot_be_less_than_zero(self):
        items = [Item(name="Conjured Mana Cake", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_conjured_cannot_be_less_than_zero_if_zero_make_zero(self):
        items = [Item(name="Conjured Mana Cake", sell_in=5, quality=-1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_conjured_item_decreases_quality_double_after_sell_in(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    # AGED BRIE
    def test_update_quality_aged_brie(self):
        items = [Item("Aged Brie", sell_in = 5, quality = 10)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)   
        self.assertEqual(4, items[0].sell_in)

    def test_aged_brie_sell_in(self):
        items = [Item("Aged Brie", sell_in = -1, quality = 10)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)   
        self.assertEqual(-2, items[0].sell_in)

    # NORMAL ITEMS
    def test_normal_items_higher_quality(self):
        items = [Item("normal", sell_in = 5, quality = 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_normal_items_longer_sell_in(self):
        items = [Item("normal", 10, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(9, items[0].sell_in)        

    def test_normal_items_quality_below_0(self):
        items = [Item("normal", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(1, items[0].sell_in) 

    def test_normal_items_modifier_of_2(self):
        items = [Item("normal", -1, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(-2, items[0].sell_in) 
        
    # SURLFURAS
    def test_sulfuras_quality(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=79)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
    
    def test_sulfuras_sell_in(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
    
if __name__ == '__main__':
    unittest.main()
