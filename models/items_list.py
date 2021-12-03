from models.item import *

item1 = Item("bread", 1.20, 1, True)
item2 = Item("milk", 1, 2, True)
item3 = Item("tomatoes", 1, 15, False)
item4 = Item("bananas", 1, 5, False)
item5 = Item("eggs", 1.50, 12, True)
item6 = Item("rocket", 0.75, 1, True)

items = [item1, item2, item3, item4, item5, item6]


def add_new_item(item):
    items.append(item)
