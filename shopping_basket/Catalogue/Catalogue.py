import copy
from shopping_basket.Singleton import Singleton
from shopping_basket.Item import Item

class Catalogue(metaclass=Singleton):

    def __init__(self):
        self._items = {}

    def add_item(self, item: Item, price: float, quantity: int):
        if quantity<=0:
            raise ValueError("Not a valid quantity")
        if price<=0:
            raise ValueError("Not a valid price")
        if item in self._items:
            self._items[item] = [price, self._items[item][1] + quantity]
        else:
            self._items[item] = [price, quantity]

    def remove_item(self, item: Item, quantity: int):
        if item not in self._items or self._items[item][1] < quantity:
            raise ValueError("Incorrect Quantity to remove")
        self._items[item][1] -= quantity
        if self._items[item][1] == 0:
            del self._items[item]

    def show_items(self):
        return copy.copy(self._items)
