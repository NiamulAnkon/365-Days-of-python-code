class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
                
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
               new_paths = self.get_paths(node, end, path)
               for p in new_paths:
                   paths.append(p)
        return paths
    
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
                    if shortest_path == None or len(sp)< len(shortest_path):
                        shortest_path = sp
                
        return shortest_path

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    routes_graph = Graph(routes)

    d = {
        "Mumbai": ["Paris", "Dubai"],
        "Paris": ["Dubai", "New York"],
    }

    start = "Paris"
    end = "New York"

    print(routes_graph.get_shortest_path(start, end))
