# -*- coding: utf-8 -*-

class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            if item.name == "Sulfuras":
                continue  # Does not change in quality or sell_in
            item.update_sell_in()
            item.update_quality()
            self._check_quality_bounds(item)

    def _check_quality_bounds(self, item):
        # Check base conditions for quality
        if item.quality < self.MIN_QUALITY:
            item.quality = self.MIN_QUALITY
        if item.quality > self.MAX_QUALITY:
            item.quality = self.MAX_QUALITY


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Subclasses that override the update_quality function of parent class Item
class AgedBrie(Item):
    def update_quality(self):
        self.quality += 1


class BackstagePasses(Item):
    def update_quality(self):
        if self.sell_in < 0:  # Concert day
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1


class Conjured(Item):
    def update_quality(self):
        self.quality -= 4 if self.sell_in < 0 else 2


class GeneralItem(Item):
    def update_quality(self):
        self.quality -= 2 if self.sell_in < 0 else 1
