import random

# Generate the initial population with a given size
def generate_population(graph, pop_size, origin, destination):
    # Remove the origin and destination from the nodes list
    nodes = list(set(graph.nodes.keys()) - {origin, destination})
    # Create the population by randomizing the order of nodes between origin and destination
    return [[origin] + random.sample(nodes, len(nodes)) + [destination] for _ in range(int(pop_size))]

# Calculate the total cost of a chromosome (path)
def total_cost(graph, chromosome):
    cost = 0
    for i in range(len(chromosome) - 1):
        cost += float(graph.nodes[chromosome[i]][chromosome[i + 1]])
    return cost

# Calculate the fitness of a chromosome (inverse of the total cost)
def fitness(graph, chromosome):
    return 1 / total_cost(graph, chromosome)

# Select two parents based on their fitness values
def selection(population, fitness_values):
    selected = random.choices(population, weights=fitness_values, k=2)
    return selected[0], selected[1]

# Perform crossover operation between two parents to produce a child
def crossover(parent1, parent2):
    # Randomly select two positions for crossover points
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    # Initialize the child with None values except for origin and destination
    child = [None] * len(parent1)
    child[0], child[-1] = parent1[0], parent1[-1]
    # Copy the segment between crossover points from parent1 to child
    child[start:end] = parent1[start:end]

    # Fill in the remaining positions in the child using parent2
    parent2_index, child_index = 1, 1
    while None in child:
        if parent2[parent2_index] not in child:
            if child_index == start:
                child_index = end
            child[child_index] = parent2[parent2_index]
            child_index += 1
        parent2_index += 1

    return child

# Perform mutation on a child by randomly swapping positions
def swap_mutation(chromosome, mutation_rate):
    for i in range(1, len(chromosome) - 1):
        if random.random() < mutation_rate:
            j = random.randint(1, len(chromosome) - 2)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Main genetic algorithm function
def genetic_algorithm(graph, origin, destination):
    # Get user inputs for the genetic algorithm parameters
    pop_size = int(input("Population Size: "))
    max_generations = int(input("Max Generation: "))
    mutation_rate = float(input("Mutation Rate: "))

    # Generate the initial population
    population = generate_population(graph, pop_size, origin, destination)

    # Evolve the population over multiple generations
    for generation in range(max_generations):
        fitness_values = [fitness(graph, chromosome) for chromosome in population]
        best_solution = population[fitness_values.index(max(fitness_values))]
        best_cost = total_cost(graph, best_solution)

        new_population = []
        for _ in range(pop_size):
            parent1, parent2 = selection(population, fitness_values)
            child = crossover(parent1, parent2)
            child = swap_mutation(child, mutation_rate)
            new_population.append(child)

        population = new_population

    # Print and return the best solution found
    print(f"Cost {best_cost}")
    return best_solution
