import unittest
from shopping_basket.Item import Item
from shopping_basket.Catalogue.Catalogue import Catalogue
from shopping_basket.Cart.Cart import Cart
from shopping_basket.Offers.PercentOffer import PercentOffer
from shopping_basket.Offers.BuynGetmOffer import BuynGetmOffer
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
        self.catalogue.clear_catalogue()
        self.catalogue.add_item(item_1, price_1, quantity_1)
        Offers().clear_offers()
        an_offer = PercentOffer("p1", 10, item_1)
        Offers().add_offer(an_offer)
        expected_discount = 20.0

        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart)
        actual_discount = cart.calculate_discount()
        assert actual_discount == expected_discount

    def test_calculate_percent_discount_on_two_items(self):
        item_1, price_1, quantity_1 = Item("an_item_1"), 100.0, 20
        item_2, price_2, quantity_2 = Item("an_item_2"), 100.0, 20
        quantity_to_add_to_cart_1 = 2
        quantity_to_add_to_cart_2 = 2
        self.catalogue.clear_catalogue()
        self.catalogue.add_item(item_1, price_1, quantity_1)
        self.catalogue.add_item(item_2, price_2, quantity_2)
        Offers().clear_offers()
        an_offer = PercentOffer("p1", 10, item_1)
        another_offer = PercentOffer("p2", 20, item_2)
        Offers().add_offer(an_offer)
        Offers().add_offer(another_offer)

        expected_discount = 60.0

        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart_1)
        cart.add_item(item_2, quantity_to_add_to_cart_2)
        actual_discount = cart.calculate_discount()
        assert actual_discount == expected_discount

    def test_calculate_sub_total(self):
        item_1, price_1, quantity_1 = Item("an_item_1"), 100.0, 20
        item_2, price_2, quantity_2 = Item("an_item_2"), 200.0, 20
        quantity_to_add_to_cart_1 = 2
        quantity_to_add_to_cart_2 = 2
        self.catalogue.clear_catalogue()
        self.catalogue.add_item(item_1, price_1, quantity_1)
        self.catalogue.add_item(item_2, price_2, quantity_2)

        expected_sub_total = 600.0

        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart_1)
        cart.add_item(item_2, quantity_to_add_to_cart_2)

        actual_sub_total = cart.calculate_sub_total()
        assert  actual_sub_total == expected_sub_total



    def test_calculate_totals(self):
        item_1, price_1, quantity_1 = Item("an_item_1"), 100.0, 20
        item_2, price_2, quantity_2 = Item("an_item_2"), 100.0, 20
        quantity_to_add_to_cart_1 = 2
        quantity_to_add_to_cart_2 = 2
        self.catalogue.clear_catalogue()
        self.catalogue.add_item(item_1, price_1, quantity_1)
        self.catalogue.add_item(item_2, price_2, quantity_2)
        Offers().clear_offers()
        an_offer = PercentOffer("p1", 10, item_1)
        another_offer = PercentOffer("p2", 20, item_2)
        Offers().add_offer(an_offer)
        Offers().add_offer(another_offer)

        expected_totals = 340.0

        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart_1)
        cart.add_item(item_2, quantity_to_add_to_cart_2)

        actual_total = cart.calculate_totals()
        assert actual_total == expected_totals


    def test_calculate_totals_for_BuynGetm(self):
        item_1, price_1, quantity_1 = Item("an_item_1"), 100.0, 20
        item_2, price_2, quantity_2 = Item("an_item_2"), 100.0, 20
        quantity_to_add_to_cart_1 = 4
        quantity_to_add_to_cart_2 = 4
        self.catalogue.clear_catalogue()
        self.catalogue.add_item(item_1, price_1, quantity_1)
        self.catalogue.add_item(item_2, price_2, quantity_2)
        Offers().clear_offers()
        an_offer = BuynGetmOffer("b1", 3, 1, item_1)
        Offers().add_offer(an_offer)

        expected_totals = 700.0

        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart_1)
        cart.add_item(item_2, quantity_to_add_to_cart_2)

        actual_total = cart.calculate_totals()
        assert actual_total == expected_totals

    def test_calculate_totals_for_BuynGetm_and_percent(self):
        item_1, price_1, quantity_1 = Item("an_item_1"), 100.0, 20
        item_2, price_2, quantity_2 = Item("an_item_2"), 100.0, 20
        quantity_to_add_to_cart_1 = 4
        quantity_to_add_to_cart_2 = 4
        self.catalogue.clear_catalogue()
        self.catalogue.add_item(item_1, price_1, quantity_1)
        self.catalogue.add_item(item_2, price_2, quantity_2)
        Offers().clear_offers()
        an_offer = BuynGetmOffer("b1", 3, 1, item_1)
        another_offer = PercentOffer("b2", 50, item_2)
        Offers().add_offer(an_offer)
        Offers().add_offer(another_offer)
        expected_totals = 500.0

        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart_1)
        cart.add_item(item_2, quantity_to_add_to_cart_2)

        actual_total = cart.calculate_totals()
        assert actual_total == expected_totals