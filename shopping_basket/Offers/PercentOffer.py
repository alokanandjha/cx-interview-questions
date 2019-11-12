from Offers.BaseOffer import BaseOffer
from Offers.Offers import Offers
from Common.Item import Item
from Catalogue.Catalogue import Catalogue


class PercentOffer(BaseOffer):

    def __init__(self, offer_name, percent, item: Item):
        if (Offers().show_offers()) == 0  and offer_name in [offer.offer_name for offer in Offers().show_offers()]:
            raise ValueError("Offer with the same name already exists")
        self.offer_name = offer_name
        self._item = item
        self._percent = percent

    def get_discount_and_remaining_items(self, items):
        """
        gets the discount by applying this offer once on the items
        ---
        Params:
            items: all items along with their quantity e.g. {item1: quantity1, item2: quantity2} where item1, item2 are of type Item, and quantity1, quantity2 are of type int
        ---
        Returns:
            discount on single application of this offer, and remaining items on which discount is not applied
        """
        discount = 0.00
        if self._item in items and items[self._item] > 0:
            item_price = Catalogue().show_items()[self._item][0]
            discount = item_price * self._percent / 100
            items[self._item] -= 1
            if items[self._item] == 0:
                del items[self._item]
        return discount, items