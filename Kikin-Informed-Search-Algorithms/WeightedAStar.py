from queue import PriorityQueue


def WeightedAStarSearch(graph, heuristics, origin, destination):
    weight = float(input("Enter w value: "))
    frontier = PriorityQueue()
    frontier.put(origin, heuristics.get_weight(origin, destination))
    came_from = {}
    cost_so_far = {origin: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == destination:
            break

        for next_node in graph.get_neighbors(current):
            new_cost = cost_so_far[current] + weight * (float(graph.get_weight(current, next_node)))
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + weight * (float(heuristics.get_weight(next_node, destination)))
                frontier.put(next_node, priority)
                came_from[next_node] = current

    # Reconstruct the path
    path = [destination]
    while path[-1] != origin:
        path.append(came_from[path[-1]])
    path.reverse()
    print(f"Cost: {cost_so_far[destination]}")
    return path
