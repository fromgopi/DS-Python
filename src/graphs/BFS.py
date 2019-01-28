class BFS:

    @staticmethod
    def min_num_edges_between_nodes(graph, start_node):
        distance = 0
        shortest_path = []
        queue = [start_node]  # FIFO
        levels = {}
        levels[start_node] = 0
        shortest_paths = {}
        shortest_paths[start_node] = ":"
        visited = [start_node]
        while len(queue) != 0:
            start = queue.pop(0)
            neighbours = graph[start]
            for neighbour, _ in neighbours.iteritems():
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
                    levels[neighbour] = levels[start] + 1
                    shortest_paths[neighbour] = shortest_paths[start] + "->" + start
        return levels, shortest_paths
