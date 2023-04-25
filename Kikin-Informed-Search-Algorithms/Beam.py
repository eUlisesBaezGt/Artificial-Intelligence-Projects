from queue import PriorityQueue


def BeamSearch(graph, heuristics, start, goal):
    beam_width = int(input("Beam width: "))
    if start == goal:
        return [start]

    frontier = PriorityQueue()
    explored = set()
    parents = {}

    frontier.put(start, heuristics.get_weight(start, goal))
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
