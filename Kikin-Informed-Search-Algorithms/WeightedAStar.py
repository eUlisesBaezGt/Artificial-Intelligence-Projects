from queue import PriorityQueue

from KAGraph import KAGraph as KAg


def WeightedAStarSearch(graph, heuristics, origin="Arad", destination="Bucharest", weight=1.3):
    frontier = PriorityQueue()
    frontier.put(origin, 0)
    came_from = {}
    cost_so_far = {origin: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == destination:
            break

        for next_node in graph.get_neighbors(current):
            new_cost = cost_so_far[current] + weight*(int(graph.get_weight(current, next_node)))
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + weight*(int(heuristics.get_weight(next_node, destination)))
                frontier.put(next_node, priority)
                came_from[next_node] = current

    # Reconstruct the path
    path = [destination]
    while path[-1] != origin:
        path.append(came_from[path[-1]])
    path.reverse()
    print(f"Cost: {cost_so_far[destination]}")
    return path


def main():
    graph = KAg.Graph()
    with open("data.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destination, weight = lines[i].split()
        graph.add_edge(origin, destination, weight)

    heuristics = KAg.Graph()
    with open("heuristics.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destination, weight = lines[i].split()
        heuristics.add_edge(origin, destination, weight)

    path = WeightedAStarSearch(graph, heuristics)

    print(f"Path: {path}")


if __name__ == "__main__":
    main()
