'''
main.py
Harry Lynch
3/19/2025
Main file for the knapsack problem-- takes user input and calls util helpers
to run the Genetic Algorithm Simulation
'''

from sack import Sack
from priority import PriorityQueue
import utils as utils
import random

# Prompt user for population size and generation size
size = int(input("How many individuals would you like the population start with? "))
gens = int(input("How many generations would you like to run? (will print the best configuration of the last gen) "))

# Don't allow negative or zero for either gens or size
if (size <= 0 or gens <= 0):
    print("\nERROR: Inputted negative or zero for the initial size or generations, please use a positive, nonzero number.")
    exit()

# Initialize a set and a pq
population = PriorityQueue()
seen = set()

print(f"Generating a population of {size} random knapsacks...")
# Create 
for i in range(0, size):
    new = Sack(contents=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    initItems = random.randint(1, 12)
    # Randomize the configuration of the new individual
    for j in range(0, initItems):
        new.addItem(random.randint(0, 11))
    # If this genome already exists in the current pop, don't include it for
    # space reasons (Has no affect ultimately as every surviving member creates
    # all possible offspring from their current configuration)
    if new in seen:
        continue
    # Add to both the set and the pq 
    seen.add(new)
    population.push(new)
    
# Run the requested number of generations
for i in range(0, gens):
    print(f"\n--------------------- RUNNING GENERATION {i} ---------------------")
    population, seen = utils.runGeneration(population, seen)
    print(f"TOTAL POPULATION SIZE AFTER GENERATION: {len(population)}")
    print(f"TOTAL UNIQUE INDIVIDUALS SEEN: {len(seen)}")
    print(f"----------------------------------------------------------------")

# Print final results 5 items at a time as the user wishes
print("====================== SIMULATION COMPLETE ========================")
print(f"There are now {len(population)} unique individuals in the population, here are 5 most fit individuals: ")
print("\nNOTE: For each individual, a genome of [1, 0, 1, ...] implies that that individual has item 1 in their bag,")
print("does not have item 2, and has item 3; ** 1 = in bag; 0 = not in bag **\n")
utils.printResults(population)
print("Thank you for conducting the simulation, have a good day.")
print("===================================================================")