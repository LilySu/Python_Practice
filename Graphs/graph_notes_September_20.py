class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges: #tuple unpacking to generate dictionary
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end] # value
        print("Graph dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

if __name__ == '__main__':
    routes = [("Mumbai", "Paris"),
              ("Mumbai", "Dubai"),
              ("Paris", "Dubai"),
              ("Paris", "New York"),
              ("Dubai", "New York"),
              ("New York", "Paris"),]
    route_graph = Graph(routes)
    start = "Mumbai"
    end = "Mumbai"
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start, end))