# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items


#  4 item types ["Brie", "Sulfuras, Hand of Ragnaros", "Backstage passes to a TAFKAL80ETC concert", "normal_item", "Conjured Item"]



    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif "Conjured" in item.name:
                self.update_conjured_item(item)
            else:
                self.update_normal_item(item)
    
    def update_aged_brie(self,item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1 
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
        self.ensure_max_quality
        
    def update_normal_item(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            modifier = 2
        else:
            modifier = 1
        item.quality = item.quality - modifier
        if item.quality < 0:
            item.quality = 0
        self.ensure_max_quality
        
    def update_sulfuras(self, item):
        item.quality = 80

    def update_conjured_item(self, item):
        if item.quality > 1:
            if item.sell_in > 0:
                item.quality -= 2
            else:
                item.quality -= 4
        if item.quality < 0:
            item.quality = 0
        item.sell_in -= 1
        self.ensure_max_quality
        
    def update_backstage_passes(self, item):
        if item.sell_in > 0:
            if item.sell_in <= 5:
                item.quality += 3
            elif item.sell_in <= 10:
                item.quality += 2
            else:
                item.quality += 1
        else:
            item.quality = 0
            
        item.sell_in -= 1
        self.ensure_max_quality(item)

    @staticmethod
    def ensure_max_quality(item):
        if item.quality > 50:
            item.quality = 50
        
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    

aged_brie = Item("Aged Brie", 1, 1)
sulfuras = Item("Sulfuras", 2, 2)

rose = GildedRose([aged_brie, sulfuras])
print(rose.items)
rose.update_quality()


