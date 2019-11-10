from shopping_basket.Catalogue.Catalogue import Catalogue
from shopping_basket.Item import Item


class Cart:

    def __init__(self):
        self._items = {}
        self._catalogue = Catalogue()

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
        return self._items