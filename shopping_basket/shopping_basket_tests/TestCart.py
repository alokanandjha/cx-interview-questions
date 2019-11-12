import unittest
from Common.Item import Item
from Catalogue.Catalogue import Catalogue
from Cart.Cart import Cart
from Offers.PercentOffer import PercentOffer
from Offers.BuynGetmOffer import BuynGetmOffer
from Offers.BuynOfXOffer import BuynOfXOffer
from Offers.Offers import Offers


class TestCart(unittest.TestCase):

    def setup(self):
        Catalogue().clear_catalogue()
        Offers().clear_offers()
        self.baked_bean = Item("BakedBean")
        self.sardines = Item("Sardines")
        self.biscuits = Item("Biscuits")
        self.shampoo_small = Item("Shampoo(Small)")
        self.shampoo_medium = Item("Shampoo (Medium)")
        self.shampoo_large = Item("Shampoo (Large)")

        catalogue = Catalogue()
        catalogue.add_item(self.baked_bean, 0.99, 100)
        catalogue.add_item(self.sardines, 1.89, 100)
        catalogue.add_item(self.biscuits, 1.20, 100)
        catalogue.add_item(self.shampoo_small, 2.00, 100)
        catalogue.add_item(self.shampoo_medium, 2.50, 100)
        catalogue.add_item(self.shampoo_large, 3.50, 100)

        baked_bean_offer = BuynGetmOffer("bakedBean2For1", 2, 1, self.baked_bean)
        sardines_offer = PercentOffer("Sardines25", 25, self.sardines)

        Offers().add_offer(baked_bean_offer)
        Offers().add_offer(sardines_offer)

    def test_scenario_2(self):
        self.setup()
        basket2 = Cart()
        basket2.add_item(self.baked_bean, 2)
        basket2.add_item(self.biscuits, 1)
        basket2.add_item(self.sardines, 2)

        assert basket2.calculate_sub_total() == 6.96
        assert basket2.calculate_discount() == 0.95
        assert basket2.calculate_totals() == 6.01

    def test_scenario_1(self):
        self.setup()
        basket1 = Cart()
        basket1.add_item(self.baked_bean, 4)
        basket1.add_item(self.biscuits, 1)

        assert basket1.calculate_sub_total() == 5.16
        assert basket1.calculate_discount() == 0.99
        assert basket1.calculate_totals() == 4.17


    def test_add_item_to_cart(self):
        item_1, price_1, quantity_1 = Item("Item_1"), 2.0, 20
        quantity_to_add_to_cart = 15
        Catalogue().add_item(item_1, price_1, quantity_1)
        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart)
        assert item_1 in cart.show_items()
        assert quantity_to_add_to_cart == cart.show_items()[item_1]
        assert Catalogue().show_items()[item_1][1] == quantity_1 - quantity_to_add_to_cart

    def test_remove_item_from_cart(self):
        item_1, price_1, quantity_1 = Item("Item_2"), 2.0, 20
        quantity_to_add_to_cart = 15
        Catalogue().add_item(item_1, price_1, quantity_1)
        cart = Cart()
        cart.add_item(item_1, quantity_to_add_to_cart)

        quantity_to_remove_from_cart = 5
        cart.remove_item(item_1, quantity_to_remove_from_cart)
        assert cart.show_items()[item_1] == quantity_to_add_to_cart - quantity_to_remove_from_cart
        assert Catalogue().show_items()[item_1][1] == quantity_1 - quantity_to_add_to_cart + quantity_to_remove_from_cart

    def test_calculate_percent_discount(self):
        item_1, price_1, quantity_1 = Item("an_item"), 100.0, 20
        quantity_to_add_to_cart = 2
        Catalogue().clear_catalogue()
        Catalogue().add_item(item_1, price_1, quantity_1)
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
        Catalogue().clear_catalogue()
        Catalogue().add_item(item_1, price_1, quantity_1)
        Catalogue().add_item(item_2, price_2, quantity_2)
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
        Catalogue().clear_catalogue()
        Catalogue().add_item(item_1, price_1, quantity_1)
        Catalogue().add_item(item_2, price_2, quantity_2)

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
        Catalogue().clear_catalogue()
        Catalogue().add_item(item_1, price_1, quantity_1)
        Catalogue().add_item(item_2, price_2, quantity_2)
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
        Catalogue().clear_catalogue()
        Catalogue().add_item(item_1, price_1, quantity_1)
        Catalogue().add_item(item_2, price_2, quantity_2)
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
        Catalogue().clear_catalogue()
        Catalogue().add_item(item_1, price_1, quantity_1)
        Catalogue().add_item(item_2, price_2, quantity_2)
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

    def test_calculate_totals_for_BuynOfXOffers(self):
        item1 = Item("item1")
        item2 = Item("item2")
        item3 = Item("item3")
        Catalogue().add_item(item1, 100.0, 10)
        Catalogue().add_item(item2, 100.0, 10)
        Catalogue().add_item(item3, 1000.0, 10)
        Offers().clear_offers()

        x = {item2, item3}
        an_offer = BuynOfXOffer(offer_name="b1", n=3, x=x)
        Offers().add_offer(an_offer)
        items = {item1: 4, item2: 4, item3: 2}
        expected_discount = 100.0
        actual_discount, _ = an_offer.get_discount_and_remaining_items(items)
        assert expected_discount == actual_discount