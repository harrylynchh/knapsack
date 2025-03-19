'''
priority.py
2/28/2025
Edited 3/19/2025 to fit the Knapsack problem
Harry Lynch
File containing definitions for the PriorityQueue class, data structure
which depends on the standard library heapq for the heap logic. Note that in this
implementation, we need a 'max-heap' which is simulated by negating importance values
as python's heapq only supports min-heaps and this is the only solution
'''
import heapq
from sack import Sack
class PriorityQueue:
    queue: list
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    def push(self, data: Sack):
        # Because heapq only supports a min-heap, declare priority as negative
        # importance such that higher absolute importance is at the top of the pq
        priority = -data.imp
        heapq.heappush(self.queue, (priority, data))
    
    def pop(self) -> Sack:
        if not self.isEmpty():
            # Grab the item from the heap priority queue, _ is a placeholder
            # since it returns a tuple.
            _, item = heapq.heappop(self.queue)
            return item;
        print("ERROR: ATTEMPTING TO POP FROM EMPTY STACK")
        return None
    
    def cull(self):
        # Removes the bottom 50% individuals, keeping only the len(queue) - n best elements
        # where n is 0.5*population_size
        n = int(len(self.queue) / 2)
        if n >= len(self.queue):
            print("ERROR: ATTEMPTING TO CULL MORE ELEMENTS THAN EXIST IN THE QUEUE")
            self.queue = []
            return

        print(f"- CULLING {n} INDIVIDUALS")
        
        # Keep only the sacks with the highest importance (second element of tuple)
        survivors = [item[1] for item in heapq.nsmallest(len(self.queue) - n, self.queue)]
        
        # Rebuild the heap with the best sacks
        self.queue = [(item.imp, item) for item in survivors]  # rebuild heap with (priority, sack)
        heapq.heapify(self.queue)
        
        return survivors


    def peek(self) -> Sack:
        return self.queue[0]