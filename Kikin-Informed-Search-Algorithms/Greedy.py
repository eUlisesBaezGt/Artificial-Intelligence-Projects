from queue import PriorityQueue

from KAGraph import KAGraph as KAg


def greedy_best_first_search(graph, heuristics, start, goal):
    if start == goal:
        return [start]

    frontier = PriorityQueue()
    explored = set()
    parents = {}

    frontier.put(start, 0)
    parents[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        explored.add(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in explored and neighbor not in frontier.queue:
                frontier.put(neighbor, heuristics.get_weight(neighbor, goal))
                parents[neighbor] = current

    return None


def main():
    graph = KAg.Graph()
    with open("graph.txt") as file:
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

    path = greedy_best_first_search(graph, heuristics, "Arad", "Bucharest")

    print(f"Path: {path}")


if __name__ == "__main__":
    main()
