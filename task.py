import heapq
import random

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        
        total_cost += cost
        
        heapq.heappush(cables, cost)

    return total_cost

def random_cost_to_connect_cables(cables):
    total_cost = 0

    while len(cables) > 1:
        
        first = cables[random.randint(0, len(cables)-1)]
        cables = [x for x in cables if x != first]
        
        second = cables[random.randint(0, len(cables)-1)]
        cables = [x for x in cables if x != second]
        
        cost = first + second
        
        total_cost += cost
        
        cables.append(cost)
        
    return total_cost

cables = [4, 3, 2, 6]
print("Cables: ")
print(cables)
print("Min cost:", min_cost_to_connect_cables(cables.copy()))
print("Random cost:", random_cost_to_connect_cables(cables.copy()))


cables = [1, 2, 5, 10, 35, 89]

print("Cables: ")
print(cables)
print("Min cost:", min_cost_to_connect_cables(cables.copy()))
print("Random cost:", random_cost_to_connect_cables(cables.copy()))

input()