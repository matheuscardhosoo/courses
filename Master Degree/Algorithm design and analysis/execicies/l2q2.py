"""
List 2 - Question 2

Given the following abstraction:
- Group with the identifiers of locals/cities: V = {v1, v2, ..., vn}.
- Group with the pairs representing roads between locals: A = {(v1, v2), (v3, v4), ...}.
- Function with roadmap costs: w = d*c/a + p
    - d (distance_function): distances for each road (km).
    - c (fuel_price): fuel price (R$/l).
    - a (vehicle_efficiency): vehicle efficiency (km/l).
    - p (toll_function): toll prices for each city (R$).
- Graph representing the map with distances for each road: G = (V, A, w).

The function resolve_cheapest_path defines the path between the origin vs and destiny vt that has
lowest price.
"""


def resolve_cheapest_path(cities, roads, distance_function, toll_function, fuel_price,
                          vehicle_efficiency, origin, destiny):

    # Define the cost function.
    def cost(road):
        _, destiny = road
        road_distance = distance_function[road]
        destiny_toll = toll_function[destiny]
        return road_distance*fuel_price/vehicle_efficiency + destiny_toll

    # Creating the adjacency list.
    adjacency_list = {city: [] for city in cities}
    for road in roads:
        road_origin, road_destiny = road
        adjacency_list[road_origin].append((cost(road), road_destiny))

    # Configuring data structures.
    has_been_visited = {}
    costs = {}
    predecessors = {}
    for city in cities:
        has_been_visited[city] = False
        costs[city] = 0 if city == origin else float('inf')
        predecessors[city] = None

    # Visits propagation.
    while False in has_been_visited.values():
        current_city = min(costs.keys(), key=(
            lambda k: costs[k] if not has_been_visited[k] else float('inf')))
        cost_to_current_city = costs[current_city]
        has_been_visited[current_city] = True

        if current_city == destiny:
            break

        for road_cost, road_destiny in adjacency_list[current_city]:
            if not has_been_visited[road_destiny]:
                cost_to_road_destiny = costs[road_destiny]
                new_path = cost_to_current_city + road_cost
                if new_path < cost_to_road_destiny:
                    costs[road_destiny] = new_path
                    predecessors[road_destiny] = current_city

    # Build origin-destiny-path array.
    origin_destiny_path = [destiny]
    current_city = destiny
    while current_city != origin:
        origin_destiny_path.append(predecessors[current_city])
        current_city = predecessors[current_city]
    origin_destiny_path.reverse()
    return origin_destiny_path


cities = ['A', 'B', 'C', 'D', 'E']
roads = [('A', 'B'), ('B', 'C'),
         ('C', 'D'), ('C', 'E'),
         ('B', 'E')]
distance_function = {('A', 'B'): 1, ('B', 'C'): 1,
                     ('C', 'D'): 1, ('C', 'E'): 1,
                     ('B', 'E'): 10}
toll_function = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
fuel_price = 1
vehicle_efficiency = 1
origin = 'A'
destiny = 'E'
path = resolve_cheapest_path(cities, roads, distance_function, toll_function, fuel_price,
                             vehicle_efficiency, origin, destiny)
print(path)
