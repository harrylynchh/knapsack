import items as items
from sack import Sack
import utils as utils
# Create a list of all the possible nodes
items = [items.Item1(), items.Item2(), items.Item3(), items.Item4(), items.Item5(), \
    items.Item6(), items.Item7(), items.Item8(), items.Item9(), items.Item10(), items.Item11(), items.Item12()]

population = set()

size = int(input("How many individuals would you like the population start with? "))
gens = int(input("How many generations would you like to run? (will print the best configuration of the last gen) "))
if (size <= 0 or gens <= 0):
    print("ERROR: Inputted negative or zero for the initial size or generations, please use a positive, nonzero number.")
    quit

    
    
