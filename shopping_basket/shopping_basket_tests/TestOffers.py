import unittest
from shopping_basket.Offers.BaseOffer import BaseOffer
from shopping_basket.Offers.Offers import Offers

class TestOffers(unittest.TestCase):
    offers = Offers()

    class AnOffer(BaseOffer):
        def __init__(self, offer_name):
            self.offer_name = offer_name

        def get_discount_and_remaining_items(self, items):
            pass

    def test_add_offer_to_Offers(self):



        an_offer = self.AnOffer("Offer1")
        self.offers.add_offer(an_offer)
        assert an_offer in  self.offers.show_offers()

    def test_remove_an_offer(self):

        offer1 = self.AnOffer("Offer1")
        self.offers.add_offer(offer1)

        if offer1 in self.offers.show_offers():
            self.offers.remove_offer(offer1)

        assert offer1 not in self.offers.show_offers()


