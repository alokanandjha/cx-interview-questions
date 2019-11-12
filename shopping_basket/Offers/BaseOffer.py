from abc import ABC, ABCMeta, abstractmethod


class BaseOffer(ABC, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, offer_name):
        self.offer_name = offer_name

    @abstractmethod
    def get_discount_and_remaining_items(self, items):
        """Should apply the offer only once to the items for maximum discount.
        ---
        Params:
            items: all items along with their quantity e.g. {item1: quantity1, item2: quantity2} where item1, item2 are of type Item, and quantity1, quantity2 are of type int
        ---
        Returns:
            Implementation of this abstract method return the discount on one application of the offer and return the remaining items on which discount is not applied.
        """