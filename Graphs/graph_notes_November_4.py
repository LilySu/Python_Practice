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

    def get_paths(self, start, end, path = []):
        path = path + [start]
        # recursion, find simple-ist case first
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        for node in self.graph_dict[start]:
            if node not in path: # check if this destination has been visited
                # if visited, it will already be in the path
                new_path = self.get_paths(node, end, path) # get paths between and append end
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


if __name__=='__main__':
    routes = [
        ('Mumbai','Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'New York'),
        ('Paris', 'Dubai'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]

    route_graph = Graph(routes)
# d = {
#     'Mumbai': ['Paris', 'Dubai'],
#     'Paris' : ['Dubai','New York']
# }
    start = "Mumbai"
    end = "New York"

    # print(f"Paths between {start} and {end}:", route_graph.get_paths(start, end))
    print(f"Shortest Path between {start} and {end}:", route_graph.get_shortest_path(start, end))

