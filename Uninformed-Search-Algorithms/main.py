import functions as f

from Graph import *
import breadth
import limited_depth
import depth
import dijkstra


# import iterative_depth
# import two_way


def main():
    weighted = True
    weights = []

    # filename = "weighted_graph.txt"
    filename = "non_weighted_graph.txt"

    graph = Graph()
    with open(filename) as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        weights.append(weight)
        graph.new_edge(origin, destiny, weight)

    # CHECK IF ALL VALUES OF WEIGHTS LIST ARE EQUAL
    for i in range(len(weights)):
        if weights[i] != weights[0]:
            print("The graph is weighted\n")
            break
        if i == len(weights) - 1:
            print("The graph is not weighted\n")
            weighted = False

    # FIXME: NODES WITH MORE THAN 1 WORD
    runner = False
    print("Origin: ", end="")
    origin = input().title()
    runner = f.check_origin(graph, origin)
    print("Destiny: ", end="")
    destiny = input().title()
    runner = f.check_destiny(graph, destiny)

    # TODO: EXECUTION TIME & OPTIMAL OPTION

    # IF GRAPH IS NOT WEIGHTED, ONLY RUN BREADTH FIRST SEARCH
    if not weighted:
        path = breadth.run(graph, origin, destiny, runner)
        f.show_path(path, origin, destiny)
    # IF GRAPH IS WEIGHTED, RUN ALL ALGORITHMS
    else:
        path = breadth.run(graph, origin, destiny, runner)
        f.show_path(path, origin, destiny)

        path = limited_depth.run(graph, origin, destiny, runner)
        f.show_path(path, origin, destiny)

        path = depth.run(graph, origin, destiny, runner)
        f.show_path(path, origin, destiny)

        path = dijkstra.run(graph, origin, destiny, runner)
        f.show_path(path, origin, destiny)


if __name__ == "__main__":
    main()
