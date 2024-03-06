"""
This code block defines and executes functions that:

Calculate betweenness centrality using Dijkstra's algorithm.

Functions:
- dijkstra_betweenness(map, origin, path_counter, cities_dict_copy):
    Calculate betweenness centrality using Dijkstra's algorithm.
    
- calculate_betweenness(map, cities_dict4a):
    Calculate betweenness centrality for cities using Dijkstra's algorithm.
    
This approach is useful for analyzing the centrality of cities within a road network, 
which can provide insights into their importance in transportation systems or social networks.
"""

from country_removal_simulation import cities_deleted_c, road_map
from dijkstra_shortest_path import dijkstra

import copy


def dijkstra_betweenness(map, origin, path_counter, cities_dict_copy):

    for destination in cities_dict_copy:
        if destination != origin:
            shortest_path = dijkstra(map, origin, destination, cities_deleted_c)
            if shortest_path != []:
                for node in shortest_path:
                    if node[0] != origin and node[0] != destination:
                        path_counter[node[0]] += 1

    # print(path_counter)
    return path_counter


def calculate_betweenness(map, cities_dict4a):

    cities_betweenness_copy = copy.deepcopy(cities_dict4a)
    # we initialize the path_counter to zeros
    path_counter = {key: 0 for key in cities_betweenness_copy.keys()}
    for city in cities_betweenness_copy:
        path_counter = dijkstra_betweenness(
            map, city, path_counter, cities_betweenness_copy
        )
        # This might run slow. Print the cities as a status indicator.
    #        print(f"{cities[city]}")

    betweenness = {}
    n = len(cities_betweenness_copy)
    for i in path_counter:
        betweenness[i] = path_counter[i] * n
    print(path_counter)
    max_city = max(betweenness, key=betweenness.get)
    print(max_city)
    max_value = betweenness[max_city]
    print(
        f"The city with the highest closeness centrality is: {cities_betweenness_copy[max_city].name} ({max_city})"
    )

    return path_counter


betweenness = calculate_betweenness(road_map, cities_deleted_c)
