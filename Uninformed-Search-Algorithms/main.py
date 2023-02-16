from Graph import *
import breadth
# import depth
# import dijkstra
# import iterative_depth
import limited_depth


# import two_way


def main():
    weight1 = True
    weight2 = True

    weights1 = []

    # WEIGHTED GRAPH
    weighted_graph = Graph()
    with open("weighted_graph.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        weights1.append(weight)
        weighted_graph.new_edge(origin, destiny, weight)

    # CHECK IF ALL VALUES OF WEIGHTS1 LIST ARE EQUAL
    for i in range(len(weights1)):
        if weights1[i] != weights1[0]:
            print("The graph 1 is not weighted")
            weight1 = False
            break
        if i == len(weights1) - 1:
            print("The graph 1 is weighted")

    # IF GRAPH1 IS NOT WEIGHTED, ONLY RUN BREADTH FIRST SEARCH
    if not weight1:
        breadth.run(weighted_graph)
    # IF GRAPH1 IS WEIGHTED, RUN ALL ALGORITHMS
    else:
        breadth.run(weighted_graph)
        # depth.run(weighted_graph)
        # dijkstra.run(weighted_graph)
        # iterative_depth.run(weighted_graph)
        limited_depth.run(weighted_graph)
        # two_way.run(weighted_graph)

    ##################
    weights2 = []

    # NON-WEIGHTED GRAPH
    non_weighted_graph = Graph()
    with open("non_weighted_graph.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        weights2.append(weight)
        non_weighted_graph.new_edge(origin, destiny, weight)

    # CHECK IF ALL VALUES OF WEIGHTS2 LIST ARE EQUAL
    for i in range(len(weights2)):
        if weights2[i] != weights2[0]:
            print("The graph 2 is not weighted")
            weight2 = False
            break
        if i == len(weights2) - 1:
            print("The graph 2 is weighted")

    # IF GRAPH2 IS NOT WEIGHTED, ONLY RUN BREADTH FIRST SEARCH
    if not weight2:
        breadth.run(non_weighted_graph)
    # IF GRAPH2 IS WEIGHTED, RUN ALL ALGORITHMS
    else:
        breadth.run(non_weighted_graph)
        # depth.run(non_weighted_graph)
        # dijkstra.run(non_weighted_graph)
        # iterative_depth.run(non_weighted_graph)
        limited_depth.run(non_weighted_graph)
        # two_way.run(non_weighted_graph)


if __name__ == "__main__":
    main()
