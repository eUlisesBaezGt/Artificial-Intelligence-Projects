from queue import PriorityQueue


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

        for neighbor in list(graph.get_neighbors(current)):
            if neighbor not in explored and neighbor not in frontier.queue:
                frontier.put(neighbor, heuristics.get_weight(neighbor, goal))
                parents[neighbor] = current

    return None
