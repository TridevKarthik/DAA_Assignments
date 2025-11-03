# Brute-force solution to the Travelling Salesman Problem (TSP) for 5 cities

# Function To Create All Permutations of the city list.
def permumations(cities):
    if len(cities) == 0:
        return [[]]
    res = []
    for i in range(len(cities)):
        rem = cities[:i] + cities[i+1:]  
        for p in permumations(rem):
            res.append([cities[i]] + p)  
    return res

dist = [
    [0, 14, 9, 7, 12],
    [14, 0, 10, 8, 6],
    [9, 10, 0, 11, 13],
    [7, 8, 11, 0, 5],
    [12, 6, 13, 5, 0]
]


cities = [0, 1, 2, 3, 4]

# creating all possible paths
paths = permumations(cities)

# getting best path with its cost.
min_cost = float('inf')
best_path = []


for path in paths:
    cost = 0
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]] 
    cost += dist[path[-1]][path[0]]  

    if cost < min_cost:
        min_cost = cost
        best_path = path


print("Best path:", ' -> '.join(map(str, best_path)))
print("Total cost:", min_cost)