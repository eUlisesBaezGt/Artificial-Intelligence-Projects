from random import shuffle

from KAGraph import KAGraph as KAg


def StochasticHillClimbing(graph, heuristcs, origin="Arad", destination="Bucharest"):
    costs = {origin: 0}
    paths = {origin: []}
    frontier = [origin]

    while frontier:
        current = frontier.pop(0)
        if current == destination:
            print(f"Cost: {costs[current]}")
            return paths[current]

        for destiny in graph.get_neighbors(current):
            weight = graph.get_weight(current, destiny)
            if destiny not in costs or costs[current] + int(weight) < costs[destiny]:
                costs[destiny] = costs[current] + int(weight)
                paths[destiny] = paths[current] + [destiny]
                frontier.append(destiny)

        shuffle(frontier)
        frontier.sort(key=lambda x: costs[x] + int(heuristcs.nodes[current][list(heuristcs.get_neighbors(current))[0]]))
        frontier = frontier[:10]

    return None


def main():
    graph = KAg.Graph()
    with open("data.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        graph.add_edge(origin, destiny, weight)

    heuristics = KAg.Graph()
    with open("heuristics.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        heuristics.add_edge(origin, destiny, weight)

    path = StochasticHillClimbing(graph, heuristics)
    path.insert(0, "Arad")

    print(f"Path: {path}")


if __name__ == "__main__":
    main()
