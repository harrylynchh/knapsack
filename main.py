from sack import Sack
from priority import PriorityQueue
import utils as utils
import random
# Create a list of all the possible nodes

size = int(input("How many individuals would you like the population start with? "))
gens = int(input("How many generations would you like to run? (will print the best configuration of the last gen) "))
if (size <= 0 or gens <= 0):
    print("ERROR: Inputted negative or zero for the initial size or generations, please use a positive, nonzero number.")
    quit

population = PriorityQueue()

print(f"Generating a population of {size} random knapsacks...")
for i in range(0, size):
    new = Sack(contents=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    initItems = random.randint(1, 12)
    for j in range(0, initItems):
        new.addItem(random.randint(0, 11))
    
    population.push(new)
for i in range(0, gens):
    print(f"\n-------------------- RUNNING GENERATION {i} --------------------")
    population = utils.runGeneration(population)
    print(f"----------------------------------------------------------------")
    
