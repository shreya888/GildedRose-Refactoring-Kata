# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_update_standard_item(self):
        """Test to check update for standard items."""
        self.assert_item_values(Item("foo", 10, 10), 9, 9)
        self.assert_item_values(Item("foo", 0, 10), -1, 8)
        self.assert_item_values(Item("foo", 1, 0), 0, 0)

    def test_update_aged_brie(self):
        """Test to check update for Aged Brie items."""
        self.assert_item_values(Item("Aged Brie", 10, 4), 9, 5)
        self.assert_item_values(Item("Aged Brie", 10, 50), 9, 50)

    def test_update_sulfuras(self):
        """Test to check update for Sulfuras items."""
        self.assert_item_values(Item("Sulfuras", 10, 40), 10, 40)
        self.assert_item_values(Item("Sulfuras", 10, 80), 10, 80)

    def test_update_backstage_passes(self):
        """Test to check update for Backstage passes."""
        self.assert_item_values(Item("Backstage passes", 10, 10), 9, 12)
        self.assert_item_values(Item("Backstage passes", 5, 10), 4, 13)
        self.assert_item_values(Item("Backstage passes", 0, 10), -1, 0)

    def test_update_conjured_passes(self):
        """Test to check update for Conjured."""
        self.assert_item_values(Item("Conjured", 10, 10), 9, 8)
        self.assert_item_values(Item("Conjured", 0, 10), -1, 6)

    def assert_item_values(self, item, expected_sell_in, expected_quality):
        """Assert statements to match the expected sell_in and quality values after updating the item."""
        gilded_rose = GildedRose([item])
        gilded_rose.update()
        self.assertEqual(expected_sell_in, item.sell_in)
        self.assertEqual(expected_quality, item.quality)


if __name__ == '__main__':
    unittest.main()