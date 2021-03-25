"""
List 2 - Question 1

Given the following abstraction:
- Group with the identifiers of the distribution centers: C = {c1, c2, ..., cn}.
- Group with the pairs of distribution centers which exchange orders: L = {{c1, c2}, {c3, c4}, ...}.
- Graph representing the system, where C are the vertices and L the edges: G = (C, L).

The function resolve_shortest_path defines the path between the origin cx and destiny cy that passes
by less distribution centers.
"""


def create_adjacency_list(vertices, edges):
    adjacency_list = {vertice: [] for vertice in vertices}
    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])
    return adjacency_list


def resolve_shortest_path(vertices, edges, origin, destiny):
    # Creating the adjacency list.
    adjacency_list = create_adjacency_list(vertices, edges)
    # Configuring vertices.
    has_been_visited = {}
    distances = {}
    predecessors = {}
    for vertice_tag in vertices:
        has_been_visited[vertice_tag] = False
        distances[vertice_tag] = float('inf')
        predecessors[vertice_tag] = None
    # Configuring origin vertice.
    has_been_visited[origin] = True
    distances[origin] = 0
    # Preparing visit queue.
    queue = list()
    queue.append(origin)
    # Visits propagation.
    while len(queue):
        vertice_0 = queue.pop(0)
        for vertice_1 in adjacency_list[vertice_0]:
            if not has_been_visited[vertice_1]:
                has_been_visited[vertice_1] = True
                distances[vertice_1] = distances[vertice_0] + 1
                predecessors[vertice_1] = vertice_0
                queue.append(vertice_1)
                if vertice_1 == destiny:
                    break
    # Build origin-destiny-path array.
    origin_destiny_path = [destiny]
    current_vertice = destiny
    while current_vertice != origin:
        origin_destiny_path.append(predecessors[current_vertice])
        current_vertice = predecessors[current_vertice]
    origin_destiny_path.reverse()
    return origin_destiny_path


distribution_centers = ['A', 'B', 'C', 'D', 'E']
relations = [['A', 'B'], ['C', 'E'],
             ['A', 'D'], ['B', 'E']]
origin = 'A'
destiny = 'C'
path = resolve_shortest_path(distribution_centers, relations, origin, destiny)
print(path)
