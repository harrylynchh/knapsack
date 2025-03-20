'''
sack.py
Harry Lynch
3/19/2025
Implementation of the Sack class- representative of a single individual in the
population.  Really is an object containing a genome (the presence of items in that Sack)
and a weight/importance that is calculated as items are added or removed.
NOTE: Is set hashable and compatible with heapq (__lt__, __hash__, __eq__ implemented)
'''
# Adjacency array representing each item in a genome's ({weight}, {importance})
VALUES = [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9), (30, 4), (30, 5) \
         , (70, 4), (20, 9), (20, 2), (60, 1)]
class Sack:
    contents: list
    weight: int
    imp: int
    
    '''
    init
    Builds a new Sack object by making a copy of another or by passing a genome as a list
    '''
    def __init__(self, contents: list = [], other = None):
        if isinstance(other, Sack):
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
    '''
    len
    defines length of a Sack as the length of it's genome
    '''
    def __len__(self):
        return len(self.contents)
    
    '''
    removeItem
    "removes" an item from a Sack by turning the gene off and decrementing weight
    and importance by the removed item's values
    '''
    def removeItem(self, index: int):
        if self.contents[index]:
            wt, imp = VALUES[index]
            self.weight -= wt
            self.imp -= imp

        self.contents[index] = 0
    
    '''
    addItem
    "adds" an item into a Sack by turning that gene on (setting to 1) and adding
    that gene's weight/importance to the total.
    NOTE: this function will not allow a Sack to go overweight
    '''
    def addItem(self, index: int):
        # Get the item values
        wt, imp = VALUES[index]
        # If the gene is already on or adding the item would put the individual
        # overweight, return and do nothing.
        if self.contents[index] or (self.weight + wt) > 250:
            return
       
        # Flip the gene on in the individual and increment Sack values
        self.contents[index] = 1
        self.weight += wt
        self.imp += imp
    
    '''
    flip
    Core genetic process that executes the single mutation on a provided gene by
    index in the genome list.  If a gene is on, flip will turn it off, and visa versa.
    '''
    def flip(self, index: int):
        if self.contents[index]:
            self.removeItem(index)
        else:
            self.addItem(index)
    
    '''
    hash
    Needed to make the Sack class set-hashable, merely declares that the identifier
    for a Sack instance is the contents of it's genome.
    '''
    def __hash__(self):
        return hash(tuple(self.contents))
    
    '''
    eq
    Needed for set operations to determine if an instance is in a set.
    '''
    def __eq__(self, other):
        return isinstance(other, Sack) and other.contents == self.contents
    
    '''
    lt
    Needed for heapq operations, note that the comparison is flipped, this is due to
    a nuance in max-heap implementations with heapq, see more in priority.py
    '''
    def __lt__(self, other):
        if type(self) != type(other):
            print(f"ERROR: TRYING TO COMPARE PancakeStack to {type(other)}")
            return False
        return self.imp > self.imp