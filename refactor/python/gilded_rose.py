# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        item_map = {
            "Aged Brie": Brie,
            "Backstage passes to a TAFKAL80ETC concert": Backstage,
            "Sulfuras, Hand of Ragnaros": Item
        }
        
        for item in self.items:
            item_class = item_map.get(item.name, Normal)
            item_class.update_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Brie(Item):
    def update_quality(self):
        self.sell_in -= 1

        if self.quality < 50:
            self.quality += 1

        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1

class Backstage(Item):
    def update_quality(self):
        self.sell_in -= 1
        
        if self.sell_in <= 0:
            self.quality = 0
            return
        
        if self.quality < 50:
            self.quality += 1
        
        if self.sell_in <= 10 and self.quality < 50:
            self.quality += 1
        
        if self.sell_in <= 5 and self.quality < 50:
            self.quality += 1

class Normal(Item):
    def update_quality(self):
        self.sell_in -= 1
                    
        if self.quality > 0:
            self.quality -= 1
        
        if self.sell_in <= 0 and self.quality > 0:
            self.quality -= 1
