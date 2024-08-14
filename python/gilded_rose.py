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
            self._update_sell_in(item)
            self._update_quality(item)
            self._check_quality_bounds(item)

    def _update_sell_in(self, item):
        item.sell_in -= 1

    def _update_quality(self, item):
        if item.name == "Aged Brie":
            item.quality += 1
        elif item.name == "Backstage passes":
            if item.sell_in < 0:  # Concert day
                item.quality = 0
            else:
                item.quality = item.quality + 3 if item.sell_in <= 5 else item.quality + 2
        elif item.name == "Conjured":
            item.quality = item.quality - 4 if item.sell_in < 0 else item.quality - 2
        else:  # general case
            item.quality = item.quality - 2 if item.sell_in < 0 else item.quality - 1

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

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
