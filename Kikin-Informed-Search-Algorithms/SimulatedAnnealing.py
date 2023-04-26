"""
From Map to Graph
Universidad Panamericana Campus Mixcoac
Inteligencia Artificial
Enrique Ulises Báez Gómez Tagle
Iván Cruz Ledesma
Mauricio Pérez Aguirre
April 26 2023
v 1.0
Main file where you can select the algorithm you want to use.
To use this file, please install our package and run file from console.
To run file, go to folder where this file is located and run:
python main.py
"""

import random
import math
import time

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
    # Calculate the percentage decrease based on the given percentage and temperature
    decrease_percentage = 100 * \
        float(percentage_to_reduce) / float(temperature)
    # Return the percentage decrease
    return decrease_percentage


def generate_random_swap_solution(current_solution):
    # This function takes a list called current_solution as input.
    indexes = random.sample(range(1, len(current_solution) - 1), 2)
    """
    This line creates a list called indexes that contains two randomly selected 
    integers from the range 1 to the length of the input list minus one. 
    The use of range(1, len(current_solution) - 1) ensures that the first and last 
    elements of the list are not included.
    """
    value_one = current_solution[indexes[0]]
    value_two = current_solution[indexes[1]]
    """
    These two lines create two variables, value_one and value_two, 
    that hold the values at the two randomly selected indexes in the input list.
    """
    swaped_solution = current_solution.copy()
    # This line creates a new list called swaped_solution which is a copy of the input list.
    swaped_solution[indexes[0]] = value_two
    swaped_solution[indexes[1]] = value_one
    """
    These two lines swap the values at the randomly selected indexes in the swaped_solution list. 
    The value at indexes[0] is replaced with value_two, and the value at indexes[1] is replaced with value_one.
    """
    return swaped_solution
    # The function returns the new list swaped_solution, which has two values randomly swapped.


def get_solution_cost(solution, graph):

    # Start with a cost of 0
    cost = 0

    # Loop through each node in the solution except the last one
    for i in range(len(solution) - 1):
        # Get the weight of the edge between the current node and the next node
        edge_weight = float(graph.get_weight(solution[i], solution[i + 1]))
        # Add the edge weight to the cost
        cost = cost + edge_weight

    # Add the weight of the last edge to the cost
    cost = cost + float(graph.get_weight(
        solution[len(solution) - 2], solution[len(solution) - 1]))

    # Return the final cost
    return cost


def simulated_annealing_result(initial_solution, initial_temperature, number_of_iterations, stop_temperature, percentage_to_reduce_temperature, graph):

    # Initialize the temperature and the current solution
    temperature = initial_temperature
    current_solution = initial_solution

    # Calculate the cost of the initial solution
    first_solution_cost = get_solution_cost(current_solution, graph)
    current_solution_cost = 0

    # Loop until the temperature reaches the stopping temperature
    while temperature >= stop_temperature:
        # Loop through a number of iterations
        for i in range(number_of_iterations):
            # Generate a new random solution by swapping two nodes in the current solution
            new_random_solution = generate_random_swap_solution(
                current_solution)

            # Calculate the costs of the current solution and the new random solution
            current_solution_cost = get_solution_cost(current_solution, graph)
            new_random_solution_cost = get_solution_cost(
                new_random_solution, graph)

            # Calculate the difference between the costs
            differences_between_costs = current_solution_cost - new_random_solution_cost

            # If the new solution is better, accept it
            if differences_between_costs >= 0:
                current_solution = new_random_solution
            # If the new solution is worse, accept it with a certain probability based on the temperature
            else:
                uniform_random_number = random.uniform(0, 1)

                acceptance_probability = math.exp(
                    differences_between_costs / temperature)

                if uniform_random_number <= acceptance_probability:
                    current_solution = new_random_solution

        # Decrease the temperature
        alpha = decrease_temperature(
            temperature, percentage_to_reduce_temperature)
        temperature = int(temperature - alpha)

    # Return the final solution and its costs
    return current_solution, first_solution_cost, current_solution_cost


def sa(graph, start):
    start_time = time.time()

    # Generate the initial solution
    initial_solution = generate_initial_solution(graph, start)

    # Run simulated annealing to find the optimal solution
    initial_temperature = float(input("Enter the initial temperature: "))
    number_of_iterations = int(input("Enter the number of iterations: "))
    stop_temperature = float(input("Enter the stop temperature: "))
    percentage_to_reduce_temperature = float(
        input("Enter the percentage to reduce temperature: "))
    result = simulated_annealing_result(initial_solution, initial_temperature, number_of_iterations, stop_temperature,
                                        percentage_to_reduce_temperature, graph)

    # Print the cost of the optimal solution and return the solution itself
    print(f"Cost: {result[2]}")

    end_time = time.time()
    print("Tiempo de ejecución: ", end_time - start_time, "segundos")
    return result[0]
