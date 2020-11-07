class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print('Graph dict:', self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    path.append(p)
        return path

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

if __name__ == "__main__":
    route = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'New York'),
        ('Paris', 'Dubai'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]

    route_graph = Graph(route)
    start = 'Mumbai'
    end = 'New York'
    print(f'Shortest path between {start} and {end}:', route_graph.get_shortest_path(start, end))