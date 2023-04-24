def steepest_hill_climb(graph, origin, destination, ht):
    
    current_path = [origin]
    
    while current_path[-1] != destination:
        current_node = current_path[-1]
        print(current_node)
        successors = [(ht[next_node], next_node) for next_node, _ in graph.content[current_node] if next_node not in current_path]
        print(successors)
        if not successors:
            return None
        else:
            (cost, next_node) = min(successors)
            print(cost, next_node)
            print(ht[current_node])
            if cost < ht[current_node]:
                current_path.append(next_node)
            else:
                return current_path
    
    return current_path