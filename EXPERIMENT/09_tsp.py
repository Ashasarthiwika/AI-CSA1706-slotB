from itertools import permutations

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]

minimum_cost = float("inf")
best_route = None

for route in permutations(cities[1:]):
    route = (0,) + route
    cost = 0

    for i in range(len(route) - 1):
        cost += distance[route[i]][route[i + 1]]

    cost += distance[route[-1]][route[0]]

    if cost < minimum_cost:
        minimum_cost = cost
        best_route = route

print("Best Route:", best_route)
print("Minimum Cost:", minimum_cost)
