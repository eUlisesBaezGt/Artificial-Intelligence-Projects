from KAGraph import KAGraph as KAg
from queue import PriorityQueue


def BeamSearch(graph, heuristics, beam_width=2, start='Arad', goal='Bucharest'):
    if start == goal:
        return [start]

    frontier = PriorityQueue()
    explored = set()
    parents = {}

    frontier.put((start, 0))
    parents[start] = None

    while not frontier.empty():
        candidates = []
        for _ in range(beam_width):
            if not frontier.empty():
                candidates.append(frontier.get())

        for candidate, _ in candidates:
            if candidate == goal:
                path = []
                while candidate is not None:
                    path.append(candidate)
                    candidate = parents[candidate]
                return path[::-1]

            explored.add(candidate)

            for neighbor in graph.get_neighbors(candidate):
                if neighbor not in explored:
                    new_cost = heuristics.get_weight(neighbor, goal)
                    priority = new_cost
                    frontier.put((neighbor, priority))
                    parents[neighbor] = candidate

    return None


def main():
    graph = KAg.Graph()
    with open("graph.txt") as file:
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

    k = int(input("Beam width: "))
    path = BeamSearch(graph, heuristics, k)

    print(f"Path: {path}")


if __name__ == "__main__":
    main()
