import copy
from Common.Singleton import Singleton
from Offers.BaseOffer import BaseOffer


class Offers(metaclass=Singleton):
    """This is single copy of the list of all offers"""
    def __init__(self):
        self._offers = []

    def add_offer(self, offer: BaseOffer):
        """
        adds offer of type BaseOffer to the list
        ---
        Params:
            offer: is a type of BaseOffer
        """
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