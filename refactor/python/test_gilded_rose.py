# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose 

class GildedRoseTest(unittest.TestCase):
    # Aged Brie
    def test_aged_brie_update_quality(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 1 == items[0].sell_in, items[0]
        assert 2 == items[0].quality, items[0]

    def test_aged_brie_update_quality_when_zero_days(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert -1 == items[0].sell_in, items[0]
        assert 2 == items[0].quality, items[0]

    def test_aged_brie_update_quality_not_more_than_50(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 1 == items[0].sell_in, items[0]
        assert 50 == items[0].quality, items[0]

    # Sulfras
    def test_sulfras_update_quality(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 3 == items[0].sell_in, items[0]
        assert 80 == items[0].quality, items[0]

    # Backstage
    def test_backstage_update_quality_less_than_10_days_left(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 4 == items[0].sell_in, items[0]
        assert 50 == items[0].quality, items[0]

    def test_backstage_update_quality_less_than_5_days_left(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 2 == items[0].sell_in, items[0]
        assert 43 == items[0].quality, items[0]
    
    def test_backstage_update_quality_not_more_than_50(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 4 == items[0].sell_in, items[0]
        assert 50 == items[0].quality, items[0]

    def test_backstage_update_quality_past_due_date(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert -1 == items[0].sell_in, items[0]
        assert 0 == items[0].quality, items[0]
    
    # Normal Item
    def test_normal_update_quality_not_more_than_50(self):
        items = [Item(name="Normal", sell_in=5, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 4 == items[0].sell_in, items[0]
        assert 19 == items[0].quality, items[0]

    def test_normal_update_quality_not_negative(self):
        items = [Item(name="Normal", sell_in=1, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert 0 == items[0].sell_in, items[0]
        assert 0 == items[0].quality, items[0]
    
    def test_normal_update_quality_past_due_date(self):
        items = [Item(name="Normal", sell_in=-2, quality=2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        assert -3 == items[0].sell_in, items[0]
        assert 0 == items[0].quality, items[0]

if __name__ == '__main__':
    unittest.main()
