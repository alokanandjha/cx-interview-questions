import unittest
from Offers.PercentOffer import PercentOffer
from Offers.Offers import Offers
from Common.Item import Item
from Catalogue.Catalogue import Catalogue


class TestOffers(unittest.TestCase):
    offers = Offers()

    def test_discount_calculation(self):
        item1 = Item("item1")
        item2 = Item("item2")
        Catalogue().add_item(item1, 100.0, 10)
        Offers().clear_offers()
        an_offer = PercentOffer(offer_name="p1", percent=10, item=item1)
        Offers().add_offer(an_offer)
        items = {item1: 1, item2: 1}
        expected_discount = 10.0
        actual_discount, _ = an_offer.get_discount_and_remaining_items(items)
        assert expected_discount == actual_discount