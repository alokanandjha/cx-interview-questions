from abc import ABC, ABCMeta, abstractmethod

class BaseOffer(ABC, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, offer_name):
        self.offer_name = offer_name

    @abstractmethod
    def get_discount_and_remaining_items(self, items):
        """Applies the offer only once to the items for maximum discount"""