from shopping_basket.Offers.BaseOffer import BaseOffer
from shopping_basket.Offers.Offers import Offers
from shopping_basket.Item import Item
from shopping_basket.Catalogue.Catalogue import Catalogue

class PercentOffer(BaseOffer):

    def __init__(self, offer_name, percent, item: Item):
        if (Offers().show_offers()) == 0  and offer_name in [offer.offer_name for offer in Offers().show_offers()]:
            raise ValueError("Offer with the same name already exists")
        self.offer_name = offer_name
        self._item = item
        self._percent = percent

    def get_discount_and_remaining_items(self, items):
        discount = 0.0
        if self._item in items and items[self._item] > 0:
            item_price = Catalogue().show_items()[self._item][0]
            discount = item_price * self._percent / 100
            items[self._item] -= 1
            if items[self._item] == 0:
                del items[self._item]
        return discount, items