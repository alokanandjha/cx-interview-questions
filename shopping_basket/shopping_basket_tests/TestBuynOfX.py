import unittest
from Offers.BuynOfXOffer import BuynOfXOffer
from Offers.Offers import Offers
from Common.Item import Item
from Catalogue.Catalogue import Catalogue


class TestOffers(unittest.TestCase):
    offers = Offers()

    def test_discount_calculation_applied_to_one_item_in_set(self):
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
        items = {item1: 4, item2: 4, item3: 3}
        expected_discount = 1000.0
        actual_discount, _ = an_offer.get_discount_and_remaining_items(items)
        assert expected_discount == actual_discount

    def test_discount_calculation_applied_to_more_items_in_set(self):
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
