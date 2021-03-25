"""
Test 2 - Question 1

Given the following inputs:
- Group of graph vertices: V = {v1, v2, ..., vn}.
- Group of graph edges: E = {{v1, v2}, {v3, v4}, ...}.

The function is_connected_graph answers the following question:
For each vertice in V, is there at least one edge in E connecting connecting it to another vertice?
"""


def create_adjacency_list(vertices, edges):
    adjacency_list = {vertice: [] for vertice in vertices}
    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])
    return adjacency_list


def is_connected_graph(vertices, edges):
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
    # Set an arbitrary vertice
    origin = vertices[0]
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
    # Check if there aren't elements with inf distances (equivalent to not connected)
    # into the distance map.
    return float('inf') not in distances.values()


vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [['A', 'B'], ['C', 'E'],
         ['A', 'D'], ['B', 'E']]
print(is_connected_graph(vertices, edges))
