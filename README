# README.md
## Harry Lynch
### 3/20/2025
### Solving the Knapsack Problem
---
# About:

    This program is designed to determine the optimal configuration of items to
    be stored in a knapsack where each item has a weight and an importance.  This
    problem is solved using a Genetic Algorithm which uses single-mutation as 
    a method of generate new individuals and a 50% cull per generation to reinforce
    natural selection.  There are twelve available items for the knapsack and the
    knapsack may not exceed a weight value of 250 (see GA.pdf for more details)
---
# Usage:

    - To run the program, execute: python main.py
    - Choose a starting population size and how many generations to run
    - After running the genetic algorithm, the program will present the top 5
      individuals in the final generation with the option to show 5 more with
      each press of the enter key, type anything to exit the program.
    - The following information is provided for each individual:
        - Their genome (a list of 0s and 1s where 1 represents that item in the bag)
        - Their total weight
        - Their total importance value
    - Each generation also shows how many individuals were culled, how many new
      offspring were added, and the total population count before/after the generation
---
# Resources:
    
    - I referenced stack overflow for the concepts of the max-heap implementation
      wherein it is still a min-heap but the priorities are negated.
    - I used heapq and random from the python stdlib to handle the priority
      queue data structure and to generate the initial population. 
      
          ** No external packages are required to run this program. **
