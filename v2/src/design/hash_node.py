class HashNode:
    """
    Hash Node class
    """
    def __init__(self, key, value):
        """
        Constructor for HashNode
        """
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
    
    def __repr__(self):
        return str(self)

        