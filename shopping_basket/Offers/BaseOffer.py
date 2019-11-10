from abc import ABC, ABCMeta, abstractmethod

class BaseOffer(ABC, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, offer_name):
        self._offer_name = offer_name

    @abstractmethod
    def apply(self, items):
        """Applies the offer only once to the items for maximum discount"""