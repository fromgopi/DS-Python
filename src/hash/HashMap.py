from src.hash.Node import Node


class HashMap:

    def __init__(self, store):
        self.store = [None for _ in range(16)]

    def get_item(self, key):
        index = hash(key) & 16
        print("Index at which key is going {}".format(index))
        if self.store[index] is None:
            return None
        item = self.store[index]
        print("item {}".format(item))
        while True:
            if item.key == key:
                return item.value
            else:
                if item.next:
                    item = item.next
                else:
                    return None