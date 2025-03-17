class Item:
    importance: int
    weight: int
    hashKey: str
    
    def __init__(self, weight, importance, hashKey):
        self.hashKey = hashKey
        self.importance = importance
        self.weight = weight
        
    def __hash__(self):
        return hash(self.hashKey)
    
    def __eq__(self, other):
        return isinstance(other, Item) and self.hashKey == other.hashKey

class Item1(Item):
    def __init__(self):
        super().__init__(20, 6, "Item1")

class Item2(Item):
    def __init__(self):
        super().__init__(30, 5, "Item2")

class Item3(Item):
    def __init__(self):
        super().__init__(60, 8, "Item3")

class Item4(Item):
    def __init__(self):
        super().__init__(90, 7, "Item4")

class Item5(Item):
    def __init__(self):
        super().__init__(50, 6, "Item5")

class Item6(Item):
    def __init__(self):
        super().__init__(70, 9, "Item6")

class Item7(Item):
    def __init__(self):
        super().__init__(30, 4, "Item7")

class Item8(Item):
    def __init__(self):
        super().__init__(30, 5, "Item8")

class Item9(Item):
    def __init__(self):
        super().__init__(70, 4, "Item9")

class Item10(Item):
    def __init__(self):
        super().__init__(20, 9, "Item10")

class Item11(Item):
    def __init__(self):
        super().__init__(20, 2, "Item11")

class Item12(Item):
    def __init__(self):
        super().__init__(60, 1, "Item12")
