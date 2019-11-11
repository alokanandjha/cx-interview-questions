import unittest
from shopping_basket.Item import Item
from shopping_basket.Catalogue.Catalogue import Catalogue
from shopping_basket.Cart.Cart import Cart
from shopping_basket.Offers.PercentOffer import PercentOffer
from shopping_basket.Offers.Offers import Offers


class TestCart(unittest.TestCase):

    catalogue = Catalogue()

    def test_add_item_to_cart(self):
        item_1, price_1, quantity_1 = Item("Item_1"), 2.0, 20
        quantity_to_add_to_cart = 15
        self.catalogue.add_item(item_1, price_1, quantity_1)
        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart)
        assert item_1 in cart.show_items()
        assert quantity_to_add_to_cart == cart.show_items()[item_1]
        assert self.catalogue.show_items()[item_1][1] == quantity_1 - quantity_to_add_to_cart

    def test_remove_item_from_cart(self):
        item_1, price_1, quantity_1 = Item("Item_2"), 2.0, 20
        quantity_to_add_to_cart = 15
        self.catalogue.add_item(item_1, price_1, quantity_1)
        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart)

        quantity_to_remove_from_cart = 5
        cart.remove_item(item_1, quantity_to_remove_from_cart)
        assert cart.show_items()[item_1] == quantity_to_add_to_cart - quantity_to_remove_from_cart
        assert self.catalogue.show_items()[item_1][1] == quantity_1 - quantity_to_add_to_cart + quantity_to_remove_from_cart

    def test_calculate_percent_discount(self):
        item_1, price_1, quantity_1 = Item("an_item"), 100.0, 20
        quantity_to_add_to_cart = 2
        expected_discount = 20.0
        self.catalogue.clear_catalogue()
        self.catalogue.add_item(item_1, price_1, quantity_1)
        Offers().clear_offers()
        an_offer = PercentOffer("p1", 10, item_1)
        Offers().add_offer(an_offer)

        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart)
        actual_discount = cart.calculate_discount()
        assert actual_discount == expected_discount




    def test_calculate_totals(self):
        pass

