# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_update_item(self):
        self.assert_item_values(Item("foo", 10, 10), 9)
        self.assert_item_values(Item("foo", 0, 10), 8)
        self.assert_item_values(Item("foo", 1, 0), 0)
        self.assert_item_values(Item("Aged Brie", 10, 4), 5)
        self.assert_item_values(Item("Aged Brie", 10, 50), 50)
        self.assert_sulfuras_values(Item("Sulfuras", 10, 40))
        self.assert_sulfuras_values(Item("Sulfuras", 10, 80))
        self.assert_item_values(Item("Backstage passes", 10, 10), 12)
        self.assert_item_values(Item("Backstage passes", 5, 10), 13)
        self.assert_item_values(Item("Backstage passes", 0, 10), 0)

    def assert_item_values(self, item, expected_quality):
        expected_sell_in = item.sell_in - 1

        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        self.assertEqual(expected_sell_in, item.sell_in)
        self.assertEqual(expected_quality, item.quality)

    def assert_sulfuras_values(self, item):
        self.assertEqual(item.name, "Sulfuras")

        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        expected_sell_in = item.sell_in
        expected_quality = item.quality

        self.assertEqual(expected_sell_in, item.sell_in)
        self.assertEqual(expected_quality, item.quality)


if __name__ == '__main__':
    unittest.main()
