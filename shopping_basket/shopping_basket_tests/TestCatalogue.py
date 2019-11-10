import unittest
from shopping_basket.Item import Item
from shopping_basket.Catalogue.Catalogue import Catalogue

class TestCatalogue(unittest.TestCase):

    def test_add_an_item_to_catalogue(self):
        first_item = Item("FirstItem")
        catalogue = Catalogue()
        catalogue.add_item(first_item, price=2.0, quantity=10)
        assert first_item in catalogue.show_items()
