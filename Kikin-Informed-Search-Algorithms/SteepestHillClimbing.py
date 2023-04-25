from KAGraph import KAGraph as KAg


def SteepestHillClimbing(graph, heuristcs, origin="Arad", destination="Bucharest"):
    costs = {origin: 0}
    paths = {origin: []}
    frontier = [origin]

    while frontier:
        frontier.sort(key=lambda node: costs[node] + int(heuristcs.nodes[node][list(heuristcs.nodes[node].keys())[0]]))
        current = frontier.pop(0)

        if current == destination:
            print(f"Cost: {costs[current]}")
            return paths[current] + [current]

        for next_node in graph.get_neighbors(current):
            weight = graph.get_weight(current, next_node)
            cost = costs[current] + int(weight)
            if next_node not in costs or cost < costs[next_node]:
                costs[next_node] = cost
                paths[next_node] = paths[current] + [current]
                if next_node not in frontier:
                    frontier.append(next_node)
    return None


def main():
    graph =KAg.Graph()
    with open("graph.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        graph.add_edge(origin, destiny, weight)

    heuristics =KAg.Graph()
    with open("heuristics.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        heuristics.add_edge(origin, destiny, weight)

    path = SteepestHillClimbing(graph, heuristics)

    print(f"Path: {path}")


if __name__ == "__main__":
    main()
