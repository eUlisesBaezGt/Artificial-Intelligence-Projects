def SteepestHillClimbing(graph, heuristcs, origin, destination):
    costs = {origin: 0}
    paths = {origin: []}
    frontier = [origin]

    while frontier:
        frontier.sort(key=lambda node: costs[node] + float(heuristcs.nodes[node][list(heuristcs.nodes[node].keys())[0]]))
        current = frontier.pop(0)

        if current == destination:
            print(f"Cost: {costs[current]}")
            return paths[current] + [current]

        for next_node in graph.get_neighbors(current):
            weight = graph.get_weight(current, next_node)
            cost = costs[current] + float(weight)
            if next_node not in costs or cost < costs[next_node]:
                costs[next_node] = cost
                paths[next_node] = paths[current] + [current]
                if next_node not in frontier:
                    frontier.append(next_node)
    return None
