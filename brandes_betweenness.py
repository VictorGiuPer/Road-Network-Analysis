"""
Brandes Betweenness Centrality

This module contains a function to calculate betweenness centrality using Brandes' algorithm.

Functions:
- brandes_betweenness(map, cities_dict):
    Calculate betweenness centrality for cities using Brandes' algorithm.

This approach efficiently computes betweenness centrality for cities in a road network, providing insights into their importance in transportation systems or social networks.
"""

from heapq import heappush, heappop
from country_removal_simulation import cities_deleted_c, road_map


def brandes_betweenness(map, cities_dict):
    # Initialize betweenness centrality dictionary
    betweenness_scores = {city: 0 for city in cities_dict.keys()}
    # Iterate over each city as source
    for origin in cities_dict.keys():
        # Single source shortest paths problem
        order_of_encounter = []
        predecessor_match = {w: [] for w in cities_dict.keys()}
        n_shortest_paths = dict.fromkeys(cities_dict.keys(), 0)
        n_shortest_paths[origin] = 1
        shortest_node_to_other = dict.fromkeys(cities_dict.keys(), float("inf"))
        shortest_node_to_other[origin] = 0
        priority_queue = []

        heappush(priority_queue, (0, origin))

        while priority_queue:
            (d, v) = heappop(priority_queue)
            order_of_encounter.append(v)
            for w in map.get(v, {}):
                # Path discovery
                current_shortest = shortest_node_to_other[v] + map[v][w]
                if shortest_node_to_other[w] > current_shortest:
                    shortest_node_to_other[w] = current_shortest
                    heappush(priority_queue, (current_shortest, w))
                    n_shortest_paths[w] = n_shortest_paths[v]
                    predecessor_match[w] = [v]
                elif current_shortest == shortest_node_to_other[w]:
                    n_shortest_paths[w] += n_shortest_paths[v]
                    predecessor_match[w].append(v)

        # Accumulation
        delta = dict.fromkeys(cities_dict.keys(), 0)
        while order_of_encounter:
            w = order_of_encounter.pop()
            for v in predecessor_match[w]:
                delta[v] += (n_shortest_paths[v] / n_shortest_paths[w]) * (1 + delta[w])
            if w != origin:
                betweenness_scores[w] += delta[w]

    # Normalize the betweenness values (optional)
    for node in betweenness_scores:
        betweenness_scores[node] /= 2

    return betweenness_scores


# Example usage:
# Assume road_map is your map and cities_dict is the dictionary of cities
betweenness_values = brandes_betweenness(road_map, cities_deleted_c)
print(betweenness_values)
highest_city = cities_deleted_c[
    max(betweenness_values, key=betweenness_values.get)
].name
print(
    f"Highest betweenness: {highest_city}",
    f"| {max(betweenness_values, key=betweenness_values.get)}",
)

"""
This algorithm has a lower time comlpexity (faster than the O(n^3)) 
because it does not search naïvely. It efficiently computes single-source 
shortest paths for each origin using algorithms like Dijkstra's for weighted graphs 
(O(m log n) per source). By processing each origin and edge only once during the 
accumulation phase, the overall complexity is reduced to O(nm log n) for weighted graphs. 
This makes it significantly faster than O(n^3). 
"""
