import copy
from Common.Item import Item
from Common.Singleton import Singleton


class Catalogue(metaclass=Singleton):

    def __init__(self):
        self._items = {}

    def add_item(self, item: Item, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Not a valid quantity")
        if price <= 0:
            raise ValueError("Not a valid price")
        if item in self._items:
            self._items[item] = [price, self._items[item][1] + quantity]
        else:
            self._items[item] = [price, quantity]

    def get_price(self, item: Item):
        return self._items[item][0]

    def get_available_quantity(self, item: Item):
        return self._items[item][1]

    def add_existing_item(self, item: Item, additional_quantity: int):
        if self._items[item] is None:
            raise LookupError("Item not found")
        price = self.get_price(item)
        self.add_item(item, price, additional_quantity)

    def remove_item(self, item: Item, quantity: int):
        if item not in self._items or self._items[item][1] < quantity:
            raise ValueError("Incorrect Quantity to remove")
        self._items[item][1] -= quantity

    def show_items(self):
        """passing a copy of catalogue to ensure catalogue can only be modified by add_item or remove_item method in catalogue"""
        return copy.copy(self._items)

    def clear_catalogue(self):
        self._items = {}

