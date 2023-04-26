"""
From Map to Graph
Universidad Panamericana Campus Mixcoac
Inteligencia Artificial
Enrique Ulises Báez Gómez Tagle
Iván Cruz Ledesma
Mauricio Pérez Aguirre
April 26 2023
Main file where you can select the algorithm you want to use.
To use this file, please install our package and run file from console.
To run file, go to folder where this file is located and run:
python main.py
"""

# Install our Graph Class Package from Test PyPi (uploaded y published by ourselves)
# Run on console / Terminal:
# pip install -i https://test.pypi.org/simple/ KAGraph==0.1.0

# if heuristics.txt is not created, run relaciones.main()

from KAGraph import KAGraph as KAg
import string
import AStar as ast
import Beam as beam
import BranchBound as bb
import Greedy as gbfs
import SimulatedAnnealing as sa
import SteepestHillClimbing as stehc
import StochasticHillClimbing as stochc
import WeightedAStar as wast
from funcs import show_path
import timeit as t


def print_menu():
    print("1) Greedy Best First Search")
    print("2) A*")
    print("3) Weighted A*")
    print("4) Beam Search")
    print("5) Branch and Bound")
    print("6) Steepest Hill Climbing")
    print("7) Stochastic Hill Climbing")
    print("8) Simulated Annealing")
    print("9) Exit")

    print("Select an option: ", end="")
    option = int(input())

    return option


def main():
    g = KAg.Graph()  # Create a Graph object to store the cities and distances
    h = KAg.Graph()  # Create a Graph object to store the heuristics

    with open("graph.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destination, weight = lines[i].split()
        g.add_edge(origin, destination, weight)

    with open("heuristics.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destination, weight = lines[i].split()
        h.add_edge(origin, destination, weight)

    print("Origin: ", end="")
    origin = input()
    origin = string.capwords(origin).translate({ord(c): None for c in string.whitespace})
    origin2 = origin.translate({ord(c): None for c in string.whitespace})
    runner1 = g.check_origin(origin2)

    print("Destiny: ", end="")
    destiny = input()
    destiny = string.capwords(destiny).translate({ord(c): None for c in string.whitespace})
    destiny2 = destiny.translate({ord(c): None for c in string.whitespace})
    runner2 = g.check_destiny(destiny2)

    origin = string.capwords(origin).translate({ord(c): None for c in string.whitespace})
    destiny = string.capwords(destiny).translate({ord(c): None for c in string.whitespace})

    path = None

    if runner1 and runner2:
        print("VALID origin and destiny")
        opt = print_menu()

        if opt == 1:
            path = gbfs.greedy_best_first_search(g, h, origin, destiny)
        elif opt == 2:
            path = ast.AStarSearch(g, h, origin, destiny)
        elif opt == 3:
            path = wast.WeightedAStarSearch(g, h, origin, destiny)
        elif opt == 4:
            path = beam.BeamSearch(g, h, origin, destiny)
        elif opt == 5:
            path = bb.BranchAndBound(g, origin, destiny)  # TODO CHECAR SI TIENE HEURISTICA
        elif opt == 6:
            path = stehc.SteepestHillClimbing(g, h, origin, destiny)
        elif opt == 7:
            path = stochc.StochasticHillClimbing(g, h, origin, destiny)
        elif opt == 8:
            path = sa.sa(g, origin)
        elif opt == 9:
            print("Bye!")
        else:
            print("INVALID option")

        show_path(path)

    else:
        print("INVALID origin or destiny")


if __name__ == "__main__":
    main()
