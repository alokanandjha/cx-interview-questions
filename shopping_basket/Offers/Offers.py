import copy
from shopping_basket.Singleton import Singleton
from shopping_basket.Offers.BaseOffer import BaseOffer

class Offers(metaclass=Singleton):

    def __init__(self):
        self._offers = []

    def add_offer(self, offer: BaseOffer):
        if offer not in self._offers:
            self._offers.append(offer)
        else:
            raise ValueError("Offer already exists")

    def remove_offer(self, offer: BaseOffer):
        if offer in self._offers:
            self._offers.remove(offer)

    def show_offers(self):
        return copy.copy(self._offers)

    def clear_offers(self):
        self._offers = []