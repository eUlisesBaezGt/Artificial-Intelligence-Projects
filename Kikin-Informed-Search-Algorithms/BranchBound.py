from queue import PriorityQueue
from KAGraph import KAGraph as KAg


def BranchAndBound(graph, origin="Arad", destination="Bucharest"):
    visited = set()
    frontier = PriorityQueue()
    # Tuple contains the current path cost, current node, and the path so far
    frontier.put((0, origin, [origin]))
    while not frontier.empty():
        cost, node, path = frontier.get()
        if node == destination:
            return cost, path
        visited.add(node)
        for neighbor, weight in graph.nodes[node].items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                bound = cost + int(weight)
                frontier.put((bound, neighbor, new_path))
    return None, None


def main():
    graph = KAg.Graph()
    with open("data.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destination, weight = lines[i].split()
        graph.add_edge(origin, destination, weight)

    cost, path = BranchAndBound(graph)

    print(f"Cost: {cost}")
    print(f"Path: {path}")


if __name__ == "__main__":
    main()
