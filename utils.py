'''
utils.py
Harry Lynch
3/20/2025
Most of the heavy lifting for running generations of the Genetic Algorithm in 
tandem with the PriorityQueue and Sack classes.
'''
from priority import PriorityQueue
from sack import Sack

'''
promptUser
Handles user input for a given prompt and multiple-choice options 
'''
def promptUser(prompt: str, options: tuple) -> str:
    choice = None
    while choice not in options:
        choice = input(f"{prompt} {options} ")
        if choice not in options:
          print(f"Unexpected input, please specify one of these options: {options}")
    return choice

'''
runGeneration
Runs a single generation of the GA, beginning by culling 50% of the population
then all surviving individuals create 12 offspring each, with each offspring
undergoing a single-mutation of a different gene.  Then print generation info
'''
def runGeneration(pop: PriorityQueue, seen: set) -> tuple[PriorityQueue, set]:
    top10, killed = pop.cull()
    
    print("Top 10 individuals in this generation:")
    for i in range(1, 11):
        if len(top10) > (i-1):
            sack = top10[i-1]
            print(f"{i}. GENOME: {sack.contents}")
            print(f"   WEIGHT: {sack.weight}")
            print(f"   IMPORTANCE: {sack.imp}\n")
        else:
            print("LESS THAN 10 INDIVIDUALS IN THE POPULATION... INTRODUCING NEW GENOMES")
            break
    # Execute a single-replacement mutation such that each surviving individual
    # creates 12 children each with a single-replacement mutation on a different
    # gene, effectively generating all possible (single-replacement) offspring
    
    # Remove dead from the seen set
    for dead in killed:
        if dead in seen:
            seen.remove(dead)
    ctr = 0
    for i in range(0, len(pop)):
        _, sack = pop.queue[i]
        for j in range(0, 12):
            new = Sack(other=sack)
            new.flip(j)
            if new in seen:
                continue
            ctr += 1
            seen.add(new)
            pop.push(new)
    
    print(f"Added {ctr} individuals")
    return (pop, seen)

'''
printResults
Helper to print 5 indiviudals from the final generaton at a time by user input
'''
def printResults(pop: PriorityQueue): 
    population = sorted(pop.queue)  
    # Print the top 5 first before prompting
    i = 0
    i = printFive(i, population)
    
    # Loopily use printFive to print the next 5 individuals until user quits
    # or there are no more individuals
    c = ""
    while c == "":
        c = input("Press enter to 5 more individuals. (Type anything to exit)")
        if c == "":
            i = printFive(i, population)
        # Don't go out of bounds
        if i >= len(population):
            print("\n No more individuals to print. \n")
            c = "BREAK LOOP"

'''
printFive
Prints five individuals from i to i+5 and all of their information
'''
def printFive(i: int, pop: list) -> int:
    for i in range (i, i+5):
        # Don't go out of bounds
        if i >= len(pop):
            return 99999999
        
        _, sack = pop[i]
        print(f"\n{i + 1}. GENOME: {sack.contents}")
        print(f"   WEIGHT: {sack.weight}")
        print(f"   IMPORTANCE: {sack.imp}")
        
    return (i + 1)