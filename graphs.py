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

    def add_edge(self, vertix_a, vertix_b, price, time):
        self.vertices[vertix_a.data].add_edge(vertix_b.data, {"price": price, "time": time})
        if not self.directed:
            self.vertices[vertix_b.data].add_edge(vertix_a.data, {"price": price, "time": time})

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


travel_destinations = Graph(directed=False)
cities = [
    Vertex("Kuwait"), Vertex("Dubai"), Vertex("Colombo"), Vertex("Male"),
    Vertex("Doha"), Vertex("Tokyo"), Vertex("Oslo")
]

for city in cities:
    travel_destinations.add_vertex(city)

travel_destinations.add_edge(cities[0], cities[1], 120, 2)
travel_destinations.add_edge(cities[0], cities[2], 200, 4)
travel_destinations.add_edge(cities[2], cities[2], 60, 1)
travel_destinations.add_edge(cities[1], cities[4], 100, 1.5)
travel_destinations.add_edge(cities[4], cities[5], 500, 11)
travel_destinations.add_edge(cities[1], cities[6], 300, 6)

print("Where are you travelling from?")
for city in travel_destinations.vertices.keys():
    print(f"- {city}")

from_city = input("From: ")

print(f"These are all the direct flights from {from_city}")
for option in travel_destinations.vertices[from_city].get_edges():
    print(f"- {option}")

to_city = input("To: ")

weight = travel_destinations.vertices[from_city].edges[to_city]
print(f"This is gonna cost you: {weight['price']} dollars and you'll be on the flight for {weight['time']} hours.")
