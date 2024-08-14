# Gilded Rose Refactoring Kata
This repository contains my solution to the [Gilded Rose Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) problem in Python. The exercise code was originally written by [Emily Bache](https://github.com/emilybache).

# Overview
The Gilded Rose Kata is a popular coding exercise designed to teach and practice refactoring techniques. This repository showcases my approach to solving the problem using Python, focusing on improving code readability, maintainability, and scalability.

## Problem Specification
For detailed specifications about the Gilded Rose problem, refer to the [requirement document](https://github.com/shreya888/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md). The problem involves managing the quality of items in a store as their `sell_in` date approaches, with various rules for different item types.

## Solution Approach
### Flowchart
Below is the flowchart that guided my refactoring process:
<img src="https://github.com/user-attachments/assets/5102bc5f-8c56-4eff-8899-f548bedb271d" alt="drawing" width="800"/>
### Steps Followed
1. **Initial Test Run**: I started by running the existing test in `test_gilded_rose.py`, which passed successfully. This test served as a baseline.
2. **Test Expansion**: I added more tests based on the provided specifications. Initially, I wrote basic tests for generic items (**`foo`**), followed by edge cases and boundary conditions for specific items - **`Aged Brie`**, **`Backstage passes`**, **`Conjured`**, and **`Sulfuras`**.
3. **Test Corrections**: Some tests failed due to naming inconsistencies between the code and specifications. I corrected these discrepancies to align the tests with the code.
4. **Test Refactoring**: I refactored the tests into distinct functions for each item type, improving readability and organization:
   1. `test_update_standard_item`
   2. `test_update_aged_brie`
   3. `test_update_sulfuras`
   4. `test_update_backstage_passes`
   5. `test_update_conjured`
   
   I also introduced an `assert_item_values` function for streamlined assertions.

5. **Code Refactoring**: With comprehensive tests in place, I moved on to refactoring the main code in gilded_rose.py. This involved renaming items and restructuring the code for clarity and maintainability.
6. **DRY and SOLID Principles**: I applied the DRY (Don't Repeat Yourself) and SOLID (S=Single-responsibility Principle, O=Open-closed Principle L=Liskov Substitution Principle I=Interface Segregation Principle D=Dependency Inversion Principle) principles to make the code more maintainable and extensible. Key changes included:
   * Introducing new functions: `update`, `_update_quality`, `_update_sell_in`, `_check_quality_bounds`, `_aged_brie_update`, `_backstage_passes_update`, `_conjured_update`, `_conjured_update`
   * Defining constants: `MAX_QUALITY`, `MIN_QUALITY`
   * Streamlining logic and using descriptive function names.
7. **Final Tests**: After refactoring, I re-ran all tests to ensure the code was functioning as expected.
8. **Adding 'Conjured' Support**: I added tests for the "Conjured" item type, which initially failed, as expected. I then implemented the necessary logic to handle "Conjured" items, and all tests passed successfully.


## Key Learnings
1. **Efficient Code Writing**: I learned to write more efficient and maintainable code.
2. **Test-Driven Development (TDD)**: This exercise reinforced the importance of the TDD cycle.
3. **Pycharm IDE Shortcuts**: I improved my efficiency by learning PyCharm IDE shortcuts from online tutorials like [this one](https://www.youtube.com/watch?v=ofR72_PxDac).
4. **Don't repeat yourself (DRY) and SOLID Principles**: I deepened my understanding of the importance of following the DRY and [SOLID](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design) principles in software development.
5. **Flowcharting**: Creating flowcharts helped me visualize and understand the problem better. For this I used [Mermaid](https://mermaid.live/) and [Draw.io](https://app.diagrams.net/).
6. **Different types of tests**: Learnt about edge case, corner case, base case, and boundary case from [here](https://softwareengineering.stackexchange.com/questions/125587/what-are-the-difference-between-an-edge-case-a-corner-case-a-base-case-and-a-b).
7. **Pytest vs Unittest**: I got to know different libararies in [Python for testing](https://realpython.com/python-testing/) and [compared](https://www.browserstack.com/guide/pytest-vs-unittest) their pros and cons.


## Code Overview
**`gilded_rose.py`**
```python 
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
```

**`test_gilded_rose.py`**
```python 
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
```



