"""
- Need Vertex and Grpahs 
    Vertex -> Class
    - Variables
        name, 
        neighbors[], -> the edges to other vertexs
         distrance, color, 
    -Functions 
        add_neighbor(v)
    Graph -> Class
    - Variables 
        vertices{}, -> Has Letter name of Vertex and Object
    -Functions 
        add_vertex(vert), add_edge(u,v), print_graph(), bfs()
"""


class Vertex:
    def __init__(self):
        self.name = n
        self.neighbors = []
        self.distance = 9999
        self.color = 'black'  # black for unseen and red for seen
        super().__init__()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        # check to make sure you add a Vertex object to the vertices
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        # both u and v in vertices
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            # cant add edge to vertices thats not there
            return False

    def print_graph(self):
        # do for loop on the keys in the vertices dict and sort them
        for key in sorted(list(self.vertices.keys())):
            print(f'{key} is {self.vertices[key].neighbors}  and {self.vertices[key].} ')
