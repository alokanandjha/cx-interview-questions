import unittest
from shopping_basket.Item import Item
from shopping_basket.Catalogue.Catalogue import Catalogue

class TestCatalogue(unittest.TestCase):

    def test_add_an_item_to_catalogue(self):
        first_item , price, quantity = Item("FirstItem"), 2.0, 10
        catalogue = Catalogue()
        catalogue.add_item(first_item, price, quantity)
        assert first_item in catalogue.show_items()
        assert price == catalogue.show_items()[first_item][0]
        assert quantity == catalogue.show_items()[first_item][1]
