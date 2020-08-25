class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = {}

    def add_edge(self, data, weight):
        self.edges[data] = weight

    def get_edges(self):
        return self.edges.keys()

class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, vertix):
        self.vertices[vertix.data] = vertix

    def add_edge(self, vertix_a, vertix_b, weight):
        self.vertices[vertix_a.data].add_edge(vertix_b.data, weight)
        if not self.directed:
            self.vertices[vertix_b.data].add_edge(vertix_a.data, weight)

    def path_exists(self, vertix_a, vertix_b):
        to_visit = [vertix_a]
        visted = []

        while to_visit:
            current_vertix = to_visit.pop(0)
            visted.append(current_vertix)
            if current_vertix == vertix_b:
                return True
            else:
                vertices = self.vertices[current_vertix].edges.keys()
                to_visit += [vertix for vertix in vertices if vertix not in visted]
        return False


kuwait = Graph(directed=False)

kuwait_city = Vertex("Kuwait City")
salmiya = Vertex("Salmiya")
shaab = Vertex("Shaab")
shuwaikh = Vertex("Shuwaikh")

kuwait.add_vertex(kuwait_city)
kuwait.add_vertex(salmiya)
kuwait.add_vertex(shaab)
kuwait.add_vertex(shuwaikh)

kuwait.add_edge(kuwait_city, shaab, 10)
kuwait.add_edge(kuwait_city, shuwaikh, 15)
kuwait.add_edge(shaab, salmiya, 20)

print(kuwait.path_exists('Kuwait City', 'Salmiya'))
print(kuwait.path_exists('Shaab', 'Shuwaikh'))