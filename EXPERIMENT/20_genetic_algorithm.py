import random

def fitness(x):
    return x * x


population = [random.randint(0, 10) for _ in range(6)]

print("Initial Population:", population)

for generation in range(5):
    population.sort(key=fitness, reverse=True)

    parents = population[:2]

    child1 = (parents[0] + parents[1]) // 2
    child2 = random.randint(
        min(parents),
        max(parents)
    )

    population = parents + [child1, child2]

    while len(population) < 6:
        population.append(random.randint(0, 10))

    print(
        "Generation",
        generation + 1,
        ":",
        population
    )

best = max(population, key=fitness)

print("Best Solution:", best)
print("Fitness:", fitness(best))
