# -*- coding: utf-8 -*-

class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items
        self.update_functions = {
            "Aged Brie": self._aged_brie_update,
            "Backstage passes": self._backstage_passes_update,
            "Conjured": self._conjured_update,
            "Sulfuras": lambda item: None  # No-op for Sulfuras
        }

    def update(self):
        for item in self.items:
            if item.name == "Sulfuras":
                continue  # Does not change in quality or sell_in
            self._update_sell_in(item)
            self._update_quality(item)
            self._check_quality_bounds(item)

    def _update_quality(self, item):
        update_function = self.update_functions.get(item.name, self._general_item_update)
        update_function(item)

    def _update_sell_in(self, item):
        item.sell_in -= 1

    def _check_quality_bounds(self, item):
        # Check base conditions for quality
        if item.quality < self.MIN_QUALITY:
            item.quality = self.MIN_QUALITY
        if item.quality > self.MAX_QUALITY:
            item.quality = self.MAX_QUALITY

    def _aged_brie_update(self, item):
        item.quality += 1

    def _backstage_passes_update(self, item):
        if item.sell_in < 0:  # Concert day
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1

    def _conjured_update(self, item):
        item.quality -= 4 if item.sell_in < 0 else 2

    def _general_item_update(self, item):
        item.quality -= 2 if item.sell_in < 0 else 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)