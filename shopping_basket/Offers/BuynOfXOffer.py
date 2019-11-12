from Offers.BaseOffer import BaseOffer
from Offers.Offers import Offers
from Catalogue.Catalogue import Catalogue


class BuynOfXOffer(BaseOffer):

    def __init__(self, offer_name, n, x):
        if (Offers().show_offers()) == 0  and offer_name in [offer.offer_name for offer in Offers().show_offers()]:
            raise ValueError("Offer with the same name already exists")

        if n < len(x):
            raise ValueError("Offer can never be applied, as not enough items to apply on")

        self.offer_name = offer_name
        self._price = lambda item: Catalogue().show_items()[item][0]

        self._n = n
        self._X = sorted(x, key=self._price, reverse=True)

    def get_discount_and_remaining_items(self, items):
        discount = 0.0

        '''items = sorted(items, key=self._price, reverse=True)'''
        items_selected_for_discount = {}

        for x in self._X:
            if sum(items_selected_for_discount.values()) < self._n:
                qty_needed_to_fill = self._n - sum(items_selected_for_discount.values())
                qty_available, qty_x = 0, 0

                if x in items:
                    qty_available = items[x]
                qty_x = qty_needed_to_fill if qty_available>qty_needed_to_fill else qty_available
                items_selected_for_discount[x] = qty_x
            if sum(items_selected_for_discount.values()) == self._n:
                for i in items_selected_for_discount:
                    items[i] -= items_selected_for_discount[i]
                    if self._price(i) < discount or discount == 0.0:
                        discount = self._price(i)
                    if items[i] == 0:
                        del items[i]
                return discount, items
        return discount, items