from random import shuffle


def StochasticHillClimbing(graph, heuristcs, origin, destination):
    costs = {origin: 0}
    paths = {origin: []}
    frontier = [origin]

    while frontier:
        current = frontier.pop(0)
        if current == destination:
            print(f"Cost: {costs[current]}")
            return [origin] + paths[current]

        for destiny in graph.get_neighbors(current):
            weight = graph.get_weight(current, destiny)
            if destiny not in costs or costs[current] + float(weight) < costs[destiny]:
                costs[destiny] = costs[current] + float(weight)
                paths[destiny] = paths[current] + [destiny]
                frontier.append(destiny)

        shuffle(frontier)
        frontier.sort(key=lambda x: costs[x] + float(heuristcs.nodes[current][list(heuristcs.get_neighbors(current))[0]]))
        frontier = frontier[:10]

    return None
