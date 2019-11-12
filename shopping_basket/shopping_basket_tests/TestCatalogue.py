import unittest
from Common.Item import Item
from Catalogue.Catalogue import Catalogue


class TestCatalogue(unittest.TestCase):
    catalogue = Catalogue()

    def test_add_an_item_to_catalogue(self):
        first_item , price, quantity = Item("FirstItem"), 2.0, 10
        self.catalogue.add_item(first_item, price, quantity)
        assert first_item in self.catalogue.show_items()
        assert price == self.catalogue.show_items()[first_item][0]
        assert quantity == self.catalogue.show_items()[first_item][1]

    def test_there_is_only_one_catalogue(self):
        an_item, price, quantity = Item("Item1"), 2.0, 10
        catalogue1 = Catalogue()
        catalogue1.add_item(an_item, price, quantity)
        catalogue2 = Catalogue()
        assert an_item in catalogue2.show_items()

    def add_two_items_in_catalogue(self):
        first_item, price1, quantity1 = Item("I1"), 2.0, 10
        second_item, price2, quantity2 = Item("I2"), 3.0, 20
        self.catalogue.add_item(first_item, price1, quantity1)
        self.catalogue.add_item(second_item, price2, quantity2)
        assert first_item in self.catalogue.show_items()
        assert second_item in self.catalogue.show_items()

    def remove_some_quantity_of_an_item_from_catalogue(self):
        item, price, quantity = Item("Item"), 2.0, 10
        self.catalogue.add_item(item, price, quantity)
        if item in self.catalogue.show_items():
            self.catalogue.remove_item(item, 4)
        assert self.catalogue.show_items()[item][1] == 6

    def remove_all_quantity_of_an_item_from_catalogue(self):
        an_item, price, quantity = Item("AnItem"), 2.0, 10
        self.catalogue.add_item(an_item, price, quantity)
        if an_item in self.catalogue.show_items():
            self.catalogue.remove_item(an_item, 10)
        assert self.catalogue.show_items()[an_item][1] == 0

    def add_more_quantity_without_adding_price(self):
        item, price, quantity = Item("Item"), 2.0, 10
        self.catalogue.add_item(item, price, quantity)
        additional_quantity = 10
        self.catalogue.add_existing_item(item, additional_quantity = additional_quantity)
        assert self.catalogue.show_items()[item][1] == 20


