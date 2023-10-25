# -*- coding: utf-8 -*-

class GildedRoseModificado(object):

    def __init__(self, items):
        self.items = items

# Método para validar el aumento de calidad del "Backstage pass"
    def increase_backstage_pass_quality(self,item):
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1

# Método para disminuir la fecha 
    def decrease_sell_in(self, item):
        if item.name !=  "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

# Método para disminuir la calidad cuando la fecha de vencimiento ha pasado
    def decrease_quality_when_sell_in_has_passed(self, item):
        if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
              item.quality -= 1

# Método para aumentar la calidad
    def increase_quality(self,item):
        if item.quality < 50:
            item.quality += 1 

 # Método para disminuir la calidad de los items "Conjured"
    def decrease_quality_conjured(self, item):
        if item.quality > 0 and item.name == "Conjured Mana Cake":
            item.quality -= 2
        else:
            item.quality -= 1

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
               self.decrease_quality_when_sell_in_has_passed(item)
               if item.name == "Conjured Mana Cake":
                   self.decrease_quality_conjured(item)
            else:
                self.increase_quality(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self.increase_backstage_pass_quality(item)    
            self.decrease_sell_in(item)
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Conjured Mana Cake":
                        self.decrease_quality_when_sell_in_has_passed(item)
                    else:
                         item.quality = 0
                else:
                    self.increase_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
