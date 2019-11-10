import unittest
from shopping_basket.Offers.PercentOffer import PercentOffer
from shopping_basket.Offers.Offers import Offers
from shopping_basket.Item import Item
from shopping_basket.Catalogue.Catalogue import Catalogue

class TestOffers(unittest.TestCase):
    offers = Offers()

    def test_discount_calculation(self):
        item1 = Item("item1")
        item2 = Item("item2")
        Catalogue().add_item(item1, 100.0, 10)
        an_offer = PercentOffer("p1", 10, item1)
        self.offers.add_offer(an_offer)
        items = {item1: 1, item2: 1}
        expected_discount = 10.0
        actual_discount = an_offer.get_discount(items)
        assert expected_discount == actual_discount