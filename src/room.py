# Implement a class to hold room information. This should have name and
# description attributes.
# A room "Has" Items, Items is an attribute of a room. (Has a)
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None # <---- Attributes
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
