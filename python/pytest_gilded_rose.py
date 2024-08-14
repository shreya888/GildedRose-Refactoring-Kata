import pytest

from gilded_rose import Item, GildedRose


# Fixtures
@pytest.fixture
def gilded_rose():
    return GildedRose([])


# Test cases
@pytest.mark.parametrize(
    "name, sell_in, quality, expected_sell_in, expected_quality",
    [
        ("foo", 10, 10, 9, 9),
        ("foo", 0, 10, -1, 8),
        ("foo", 1, 0, 0, 0),
    ],
)
def test_update_standard_item(name, sell_in, quality, expected_sell_in, expected_quality):
    """Test to check update for standard items using parametrization."""
    item = Item(name, sell_in, quality)
    assert_item_values(item, expected_sell_in, expected_quality)


@pytest.mark.parametrize(
    "sell_in, quality, expected_sell_in, expected_quality",
    [
        (10, 4, 9, 5),
        (10, 50, 9, 50),
    ],
)
def test_update_aged_brie(sell_in, quality, expected_sell_in, expected_quality):
    """Test to check update for Aged Brie items using parametrization."""
    item = Item("Aged Brie", sell_in, quality)
    assert_item_values(item, expected_sell_in, expected_quality)


@pytest.mark.parametrize(
    "sell_in, quality",
    [
        (10, 40),
        (10, 80),
    ],
)
def test_update_sulfuras(sell_in, quality):
    """Test to check update for Sulfuras items using parametrization."""
    item = Item("Sulfuras", sell_in, quality)
    assert_item_values(item, sell_in, quality)


@pytest.mark.parametrize(
    "sell_in, quality, expected_sell_in, expected_quality",
    [
        (10, 10, 9, 12),
        (5, 10, 4, 13),
        (0, 10, -1, 0),
    ],
)
def test_update_backstage_passes(sell_in, quality, expected_sell_in, expected_quality):
    """Test to check update for Backstage passes using parametrization."""
    item = Item("Backstage passes", sell_in, quality)
    assert_item_values(item, expected_sell_in, expected_quality)


@pytest.mark.parametrize(
    "sell_in, quality, expected_sell_in, expected_quality",
    [
        (10, 10, 9, 8),
        (0, 10, -1, 6),
    ],
)
def test_update_conjured(sell_in, quality, expected_sell_in, expected_quality):
    """Test to check update for Conjured items using parametrization."""
    item = Item("Conjured", sell_in, quality)
    assert_item_values(item, expected_sell_in, expected_quality)


# Helper function
def assert_item_values(item, expected_sell_in, expected_quality):
    """Helper function to assert item values."""
    gilded_rose = GildedRose([item])
    gilded_rose.update()
    assert expected_sell_in == item.sell_in
    assert expected_quality == item.quality