from globals import VALUES
class Sack:
    contents: list
    weight: int
    imp: int
    
    def __init__(self, contents: list = [], other = None):
        if isinstance(other, Sack):
            print("RUNNING")
            # shallow cpy of the contents to avoid pass by ref
            self.contents = other.contents[:]
            self.weight = other.weight
            self.imp = other.imp
        else:
            self.contents = contents
            self.weight = 0
            self.imp = 0
            for i in range(0, len(contents)):
                if contents[i]:
                    wt, imp = VALUES[i]
                    self.weight += wt
                    self.imp += imp
    
    def __len__(self):
        return len(self.contents)
    
    def removeItem(self, index: int):
        print(f"CONTENT TYPE: {type(self.contents)}")
        if self.contents[index]:
            wt, imp = VALUES[index]
            self.weight -= wt
            self.imp -= imp

        self.contents[index] = 0
    
    def addItem(self, index: int):
        # Prevent duplicates
        wt, imp = VALUES[index]
        
        if self.contents[index] or (self.weight + wt) > 250:
            return
        
        self.contents[index] = 1
        
        self.weight += wt
        self.imp += imp

    def flip(self, index: int):
        if self.contents[index]:
            self.removeItem(index)
        else:
            self.addItem(index)
    
    def __eq__(self, other):
        return isinstance(other, Sack) and other.contents == self.contents
    
    def __lt__(self, other):
        if type(self) != type(other):
            print(f"ERROR: TRYING TO COMPARE PancakeStack to {type(other)}")
            return False
        return self.imp > self.imp