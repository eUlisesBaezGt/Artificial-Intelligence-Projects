import functions as f
import timeit as t
import string

from Graph import *
import breadth
import limited_depth
import depth
import dijkstra
import iterative_depth
import two_way


def main():
    weighted = True
    weights = []
    times = []

    filename = "weighted_graph.txt"
    # filename = "non_weighted_graph.txt"

    graph = Graph()
    with open(filename) as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        weights.append(weight)
        graph.new_edge(origin, destiny, weight)

    for i in range(len(weights)):
        if weights[i] != weights[0]:
            print("The graph is weighted\n")
            break
        if i == len(weights) - 1:
            print("The graph is not weighted\n")
            weighted = False

    print("Origin: ", end="")
    origin = input()
    origin2 = origin.translate({ord(c): None for c in string.whitespace})
    runner1 = f.check_origin(graph, origin2)
    print("Destiny: ", end="")
    destiny = input()
    destiny2 = destiny.translate({ord(c): None for c in string.whitespace})
    runner2 = f.check_destiny(graph, destiny2)

    runner = runner1 and runner2
    reached = False

    origin = string.capwords(origin).translate({ord(c): None for c in string.whitespace})
    destiny = string.capwords(destiny).translate({ord(c): None for c in string.whitespace})

    graph.view_all()

    stime = t.default_timer()
    path = breadth.run(graph, origin, destiny, runner)
    ftime = t.default_timer()
    times.append(ftime - stime)
    f.show_path(path)

    if weighted and runner:
        limit = int(input("\nEnter the limit: "))
        stime = t.default_timer()
        path = limited_depth.run(graph, origin, destiny, runner, limit)
        ftime = t.default_timer()
        times.append(ftime - stime)
        f.show_path(path)
        if path:
            reached = True

        stime = t.default_timer()
        path = depth.run(graph, origin, destiny, runner)
        ftime = t.default_timer()
        times.append(ftime - stime)
        f.show_path(path)

        stime = t.default_timer()
        path = iterative_depth.run(graph, origin, destiny, runner)
        ftime = t.default_timer()
        times.append(ftime - stime)
        f.show_path(path)

        stime = t.default_timer()
        path, weight = dijkstra.run(graph, origin, destiny, runner)
        ftime = t.default_timer()
        times.append(ftime - stime)
        f.show_path_dijkstra(path, weight)

        stime = t.default_timer()
        path = two_way.run(graph, origin, destiny, runner)
        ftime = t.default_timer()
        times.append(ftime - stime)
        f.show_path(path)

    if runner:
        print("\n\nEXECUTION TIMES:\n----------------")
        if times:
            print("Breadth First Search: ", times[0])
        if weighted and times:
            if reached:
                print("Limited Depth First Search: ", times[1])
            else:
                print("Limited Depth First Search: No path found.")
                times[1] = 999999999999
            print("Depth First Search: ", times[2])
            print("Iterative Depth Search: ", times[3])
            print("Dijkstra: ", times[4])
            print("Two Way Search: ", times[5])

            best = min(times)
            print("\nBest time: ", best)
            if best == times[0]:
                print("Breadth First Search is the best option")
            elif best == times[1] and reached:
                print("Limited Depth First Search is the best option")
            elif best == times[2]:
                print("Depth First Search is the best option")
            elif best == times[3]:
                print("Iterative Depth Search is the best option")
            elif best == times[4]:
                print("Dijkstra is the best option")
            elif best == times[5]:
                print("Two Way Search is the best option")


if __name__ == "__main__":
    main()
