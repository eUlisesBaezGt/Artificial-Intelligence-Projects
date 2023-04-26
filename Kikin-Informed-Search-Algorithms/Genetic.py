import random


# This function initializes a population of paths from a given origin to a destination
# using a graph representation of the cities and the number of paths in the population.

# This function initializes a population of paths from a given origin to a destination
# using a graph representation of the cities and the number of paths in the population.

def initialize_population(graph, origin, destination, population_size):
    # Create an empty list to hold the population of paths.
    population = []
    # Loop through the population size to generate random paths for each individual in the population.
    for _ in range(population_size):
        # Add the origin city to the path.
        path = [origin]
        # Set the current city to the origin.
        current = origin
        # While the current city is not the destination, keep adding cities to the path.
        while current != destination:
            # Get the neighbors of the current city from the graph.
            neighbors = graph.get_neighbors(current)
            # Choose a random neighbor from the list of neighbors.
            next_city = random.choice(list(neighbors))
            # Add the chosen neighbor to the path and update the current city.
            path.append(next_city)
            current = next_city
        # Add the completed path to the population.
        population.append(path)
    # Return the population of paths.
    return population


# This function calculates the fitness of a given path using the graph representation of the cities.

def fitness_function(graph, path):
    # Check if the graph and path are valid inputs, and the path has at least two cities.
    if graph is None or path is None or len(path) < 2:
        return float('inf')
    # Check if any city has already been visited more than once.
    if len(set(path)) != len(path):
        return float('inf')
    # Initialize the cost to zero.
    cost = 0
    # Loop through the cities in the path, and calculate the cost of the path.
    for i in range(len(path) - 1):
        # Get the first city of the current edge.
        node1 = path[i]
        # Get the second city of the current edge.
        node2 = path[i + 1]
        # Check if the second city is a neighbor of the first city.
        if node2 not in graph.get_neighbors(node1):
            # If node2 is not a neighbor of node1, the edge is missing, return infinity.
            return float('inf')
        # Get the weight of the edge between the two cities.
        weight = graph.get_weight(node1, node2)
        # Check if the weight of the edge is empty or None.
        if not weight:
            # If the weight is empty or None, the edge is missing, return infinity.
            return float('inf')
        # Add the weight of the edge to the cost.
        cost += int(weight)
    # If the cost of the path is less than or equal to zero, return infinity.
    if cost <= 0:
        return float('inf')

    # Return the fitness of the path, which is the inverse of the cost.
    return 1 / cost


# This function selects two individuals from the population for the next generation, based on their fitness values.

def selection(population, fitness_values):
    # Calculate the total fitness of the population.
    total_fitness = sum(fitness_values)
    # If the total fitness is zero, set the normalized fitness to an equal value for each individual in the population.
    if total_fitness == 0:
        normalized_fitness = [1 / len(population)] * len(population)
    # Otherwise, calculate the normalized fitness for each individual in the population.
    else:
        normalized_fitness = [f / total_fitness for f in fitness_values]
    # Use the normalized fitness as weights to randomly select two individuals from the population.
    selected = random.choices(population, weights=normalized_fitness, k=2)
    # Return the two selected individuals.
    return selected[0], selected[1]


# This function performs crossover between two parents to generate two offspring.
def crossover(parent1, parent2):
    # Check if the length of the parent1 is less than or equal to 2, if yes, return the parents as offspring.
    if len(parent1) <= 2:
        return parent1, parent2
    # Otherwise, randomly select a crossover point between the first and the last city of the parent1.
    crossover_point = random.randint(1, len(parent1) - 2)
    # Generate the first offspring by taking the cities from the parent1 before the crossover point
    # and adding the cities from parent2 that are not already in the offspring.
    offspring1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    # Generate the second offspring by taking the cities from the parent2 before the crossover point
    # and adding the cities from parent1 that are not already in the offspring.
    offspring2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    # Return the two offspring.
    return offspring1, offspring2


# This function performs mutation on an offspring by replacing two cities with their neighboring unvisited cities.
def mutation(graph, offspring):
    # Check if the length of the offspring is less than or equal to 3, if yes, return the offspring as it is.
    if len(offspring) <= 3:
        return offspring
    # Loop until a mutation is successfully performed.
    while True:
        # Select two distinct indices from the offspring.
        index1, index2 = random.sample(range(1, len(offspring) - 1), 2)
        # Get the two cities to be mutated.
        city1 = offspring[index1]
        city2 = offspring[index2]
        # Get the neighbors of the two cities from the graph.
        neighbors1 = list(graph.get_neighbors(city1))
        neighbors2 = list(graph.get_neighbors(city2))
        # Check if the selected cities are already present in the path.
        if city1 in offspring[:index1] + offspring[index1 + 1:index2] + offspring[index2 + 1:]:
            continue
        if city2 in offspring[:index1] + offspring[index1 + 1:index2] + offspring[index2 + 1:]:
            continue
        # Check if there are neighboring unvisited cities available to replace the old ones.
        new_city1 = None
        new_city2 = None
        for neighbor in neighbors1:
            if neighbor not in offspring:
                new_city1 = neighbor
                break
        for neighbor in neighbors2:
            if neighbor not in offspring:
                new_city2 = neighbor
                break
        # If no unvisited neighboring city is found, skip the iteration and try again.
        if new_city1 is None or new_city2 is None:
            continue
        # Replace the selected cities with the new ones.
        offspring[index1] = new_city1
        offspring[index2] = new_city2
        # Check if the new offspring has a different path than the parent.
        if len(set(offspring)) == len(offspring):
            break
    # Return the mutated offspring.
    return offspring


# This function implements the genetic algorithm for solving the traveling salesman problem.

def genetic_algorithm(graph, origin, destination):
    # Get the parameters for the genetic algorithm from the user.
    population_size = int(input("Population Size: "))
    num_generations = int(input("Number of generations: "))
    mutation_rate = float(input("Mutation rate: "))
    # Initialize the population of paths.
    population = initialize_population(graph, origin, destination, population_size)
    # Loop through the specified number of generations.
    for _ in range(num_generations):
        # Calculate the fitness values for each path in the population.
        fitness_values = [1 / fitness_function(graph, path) for path in population]
        # Create a new population by selecting parents, performing crossover and mutation, and adding the offspring
        # to the new population.
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                offspring1 = mutation(graph, offspring1)
            if random.random() < mutation_rate:
                offspring2 = mutation(graph, offspring2)
            new_population.extend([offspring1, offspring2])
        # Replace the old population with the new population.
        population = new_population
        # Check if the destination is already the last city in the path for the best path in the population.
        best_path = min(population, key=lambda x: fitness_function(graph, x))
        if best_path[-1] == destination:
            best_cost = fitness_function(graph, best_path)
            print(f"Cost: {best_cost}")
            return best_path
    # Get the best path from the final population and calculate its fitness value.
    best_path = min(population, key=lambda x: fitness_function(graph, x))
    best_cost = fitness_function(graph, best_path)
    # Print the cost of the best path and return the best path.
    print(f"Cost: {best_cost}")
    return best_path

# The genetic algorithm works best when the selected cities are close together on the map. Choosing cities that are
# too far apart will cause the algorithm to take longer to converge. To avoid this limitation, it is recommended to
# choose two cities that are close together on the map.
