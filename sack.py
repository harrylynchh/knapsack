class Sack:
    contents: set
    total_weight: int
    total_importance: int
    
    def __init__(self, contents: set):
        self.contents = contents
        self.total_weight = 0
        self.total_importance = 0
        for node in contents:
            self.total_weight += node.weight
            self.total_importance += node.importance
    
    def __len__(self):
        return len(self.contents)
    
    def removeItem(self) -> any:
        node = self.contents.pop()
        self.total_weight -= node.weight
        self.total_importance -= node.importance
        return node
    
    def addItem(self, item):
        # Prevent duplicates
        if any(isinstance(x, type(item)) for x in self.contents):
            return
        self.contents.append(item)
        self.total_weight += item.weight
        self.total_importance += item.importance
        
    def __hash__(self):
        return hash(frozenset(self.contents))
    
    def __eq__(self, other):
        return isinstance(other, Sack) and other.contents == self.contents