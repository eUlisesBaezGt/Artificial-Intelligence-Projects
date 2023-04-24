import random
import math

from KAGraph import KAGraph as KAg

def generate_initial_solution(graph, start):
    # GET ALL THE CONNECTIONS OF THE START NODE AND ADD THEM TO THE SOLUTION
    # SEARCH FOR THE START NODE IN THE GRAPH USING DICTIONARY KEY
    for node in graph.nodes:
        # IF THE NODE IS THE START NODE
        if node == start:
            # GET THE CONNECTIONS OF THE START NODE
            connections = list(graph.get_neighbors(node))
            # ADD THE START NODE TO THE SOLUTION
            connections.insert(0, start)
            # ADD THE START NODE TO THE SOLUTION
            connections.append(start)
            # RETURN THE SOLUTION
            return connections

    # IF THE START NODE IS NOT FOUND IN THE GRAPH
    print("Start node not found in graph")
    return []


def decrease_temperature(temperature, percentage_to_reduce):
    decrease_percentage = 100 * float(percentage_to_reduce) / float(temperature)
    return decrease_percentage


def generate_random_swap_solution(current_solution):
    indexes = random.sample(range(1, len(current_solution) - 1), 2)
    value_one = current_solution[indexes[0]]
    value_two = current_solution[indexes[1]]
    swaped_solution = current_solution.copy()
    swaped_solution[indexes[0]] = value_two
    swaped_solution[indexes[1]] = value_one
    return swaped_solution


def get_solution_cost(solution, graph):
    cost = 0

    for i in range(len(solution) - 1):
        cost = cost + graph.get_weight(solution[i], solution[i + 1])

    cost = cost + graph.get_weight(solution[len(solution) - 2], solution[len(solution) - 1])

    return cost


def simulated_annealing_result(initial_solution, initial_temperature, number_of_iterations, stop_temperature,
                               percentage_to_reduce_temperature, graph):
    temperature = initial_temperature
    current_solution = initial_solution

    first_solution_cost = get_solution_cost(current_solution, graph)
    current_solution_cost = 0

    while temperature >= stop_temperature:
        for i in range(number_of_iterations):
            new_random_solution = generate_random_swap_solution(current_solution)

            current_solution_cost = get_solution_cost(current_solution, graph)
            new_random_solution_cost = get_solution_cost(new_random_solution, graph)

            diferences_between_costs = current_solution_cost - new_random_solution_cost

            if diferences_between_costs >= 0:
                current_solution = new_random_solution
            else:
                uniform_random_number = random.uniform(0, 1)

                acceptance_probability = math.exp(diferences_between_costs / temperature)

                if uniform_random_number <= acceptance_probability:
                    current_solution = new_random_solution

        alpha = decrease_temperature(temperature, percentage_to_reduce_temperature)
        temperature = int(temperature - alpha)

    return current_solution, first_solution_cost, current_solution_cost


def print_simulated_annealing_result(result, initial_solution):
    print('\nInitial solution = ', initial_solution)
    print('\nInitial solution cost = ', result[1])
    print('\nSimulated annealing solution = ', result[0])
    print('\nSimulated annealing solution cost = ', result[2])


def main():
    # CREATE THE GRAPH
    graph = KAg.Graph()

    # ADD THE EDGES
    graph.add_edge("Sibiu", "Rimnicu Vilcea", 80)
    graph.add_edge("Sibiu", "Fagaras", 99)
    graph.add_edge("Rimnicu Vilcea", "Craiova", 146)
    graph.add_edge("Rimnicu Vilcea", "Pitesti", 97)
    graph.add_edge("Craiova", "Pitesti", 138)
    graph.add_edge("Pitesti", "Bucharest", 101)
    graph.add_edge("Fagaras", "Bucharest", 211)
    graph.add_edge("Sibiu", "Craiova", 1000)
    graph.add_edge("Sibiu", "Pitesti", 1000)
    graph.add_edge("Sibiu", "Bucharest", 1000)
    graph.add_edge("Rimnicu Vilcea", "Bucharest", 1000)
    graph.add_edge("Rimnicu Vilcea", "Fagaras", 1000)
    graph.add_edge("Craiova", "Bucharest", 1000)
    graph.add_edge("Fagaras", "Craiova", 1000)
    graph.add_edge("Fagaras", "Pitesti", 1000)

    origin = input("Enter the origin: ")

    # GET THE INITIAL SOLUTION
    initial_solution = generate_initial_solution(graph, origin)

    # GET THE SIMULATED ANNEALING RESULT
    result = simulated_annealing_result(initial_solution, 1000, 100, 1, 0.1, graph)

    # PRINT THE SIMULATED ANNEALING RESULT
    print_simulated_annealing_result(result, initial_solution)

main()