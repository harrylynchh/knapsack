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

def runGeneration(pop: PriorityQueue) -> PriorityQueue:
    top10 = pop.cull()
    
    print("Top 10 individuals in this generation:")
    for i in range(1, 11):
        if len(top10) > i:
            sack = top10[i-1]
            print(f"{i}. GENOME: {sack.contents}")
            print(f"   WEIGHT: {sack.weight}")
            print(f"   IMPORTANCE: {sack.imp}\n")
    # Execute a single-replacement mutation such that each surviving individual
    # creates 12 children each with a single-replacement mutation on a different
    # gene, effectively generating all possible (single-replacement) offspring
    for sack in pop.queue:
        for i in range(0, 12):
            new = Sack(other=sack)
            print(i)
            new.flip(i)
            pop.push(new)
        
    return pop