import depth as b


def bidirectional(graph, graph2, origin, destiny):
    departure = True
    arrival = True
    if not b.depth_first_search(graph, origin, destiny):
        departure = False
    if not b.depth_first_search(graph2, destiny, origin):
        arrival = False

    if departure and arrival:
        queue1 = [[origin]]
        queue2 = [[destiny]]
        while queue1 and queue2:
            path1 = queue1.pop(0)
            node1 = path1[-1]
            path2 = queue2.pop(0)
            node2 = path2[-1]
            if node1 == destiny:
                return path1
            if node2 == origin:
                path2.reverse()
                return path2
            for neighbor in graph.content[node1]:
                new_path = list(path1)
                new_path.append(neighbor[0])
                queue1.append(new_path)
            for neighbor in graph2.content[node2]:
                new_path = list(path2)
                new_path.append(neighbor[0])
                queue2.append(new_path)
    else:
        return None


def run(graph, graph2, origin, destiny, runner):
    if runner:
        print("\n\nBidirectional Search:\n--------------")
        path = bidirectional(graph, graph2, origin, destiny)
        if path:
            return path
        else:
            print("No path found.")
            return None
