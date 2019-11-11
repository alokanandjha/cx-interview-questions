import copy
from shopping_basket.Catalogue.Catalogue import Catalogue
from shopping_basket.Item import Item
from shopping_basket.Offers.Offers import Offers



class Cart:

    def __init__(self):
        self._items = {}
        self._catalogue = Catalogue()
        self._sub_total = 0.0
        self._discount = 0.0

    def add_item(self, item: Item, quantity: int):
        if quantity <= 0 or quantity > self._catalogue.show_items()[item][1]:
            raise ValueError("Not a valid quantity")
        self._catalogue.remove_item(item, quantity)
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity

    def remove_item(self, item: Item, quantity: int):
        if item not in self._items or self._items[item] < quantity:
            raise ValueError("Incorrect Quantity")
        self._items[item] -= quantity
        self._catalogue.add_existing_item(item, quantity)

    def show_items(self):
        return copy.copy(self._items)

    def calculate_discount(self):
        return self._calc_disc(Offers().show_offers(), self.show_items())


    def _calc_disc(self, offer_list, remaining_items):
        if len(offer_list) == 0 or len(remaining_items) == 0:
            return 0.0
        discount_summary = []

        for offer in offer_list:
            discount, ri = offer.get_discount_and_remaining_items(remaining_items)
            offer_list1 = copy.copy(offer_list)
            if discount == 0.0:
                offer_list1.remove(offer)
            else:
                discount_summary.append(discount + self._calc_disc(offer_list1, ri))
        if not discount_summary:
            return 0.0

        return max(discount_summary)

    def calculate_sub_total(self):
        sub_total = 0.0
        for item in self._items:
            sub_total += Catalogue().show_items()[item][0] * self._items[item]
        return sub_total


    def calculate_totals(self):
        return self.calculate_sub_total() - self.calculate_discount()