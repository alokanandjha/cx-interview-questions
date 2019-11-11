import unittest
from shopping_basket.Offers.BuynGetmOffer import BuynGetmOffer
from shopping_basket.Offers.Offers import Offers
from shopping_basket.Item import Item
from shopping_basket.Catalogue.Catalogue import Catalogue

class TestOffers(unittest.TestCase):
    offers = Offers()

    def test_discount_calculation(self):
        item1 = Item("item1")
        item2 = Item("item2")
        Catalogue().add_item(item1, 100.0, 10)
        Catalogue().add_item(item2, 100.0, 10)
        Offers().clear_offers()
        an_offer = BuynGetmOffer(offer_name="b1", n=2, m=1, item=item1)
        Offers().add_offer(an_offer)
        items = {item1: 4, item2: 4}
        expected_discount = 100.0
        actual_discount, _ = an_offer.get_discount_and_remaining_items(items)
        assert expected_discount == actual_discount