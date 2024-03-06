"""
This code block defines and executes a function that calculates the closeness centrality for 
each city in a road network. The closeness centrality is a measure of how central a node is 
within a network, based on the average length of the shortest path from the node to all other nodes.

Here's what the function does:

Iterates over each city in the provided cities_dict4d as the origin.

For each origin, it computes the shortest path length to all other cities.

Sums these path lengths to calculate the total distance.

Determines the closeness centrality for the origin city by dividing the 
total number of cities minus one by the total distance.

If a city is unreachable from the origin, it continues to the next city 
without adding to the total distance.

Collects and returns the closeness centrality values for all cities in a dictionary.

After computing the closeness centrality values, the code finds and 
prints the city with the highest closeness centrality, indicating 
it has the shortest average distance to all other cities.

The afore created brandes_betweenness function is called at the end, 
which calculates betweenness centrality for each city.

With this we create the database that will be processed and visualized in the next cell.
"""

from country_removal_simulation import cities_deleted_c, road_map
from dijkstra_shortest_path import dijkstra
from brandes_betweenness import brandes_betweenness
from city_country_distribution import roads_dict, cities_dict, countries_dict
import copy


def calculate_closeness_centrality(map, cities_dict4d):

    # create copy
    cities_copy4d = copy.deepcopy(cities_dict4d)

    closeness_centrality = {}

    for origin in cities_dict.keys():
        total_distance = 0
        for destination in cities_dict.keys():
            if origin != destination:
                shortest_path_lenght = len(
                    dijkstra(map, origin, destination, cities_copy4d)
                )
                if shortest_path_lenght:
                    total_distance += shortest_path_lenght - 1  # exclude origin
                else:
                    continue

        if total_distance:
            closeness_centrality[origin] = (len(cities_dict) - 1) / total_distance
        else:
            closeness_centrality[origin] = 0

    return closeness_centrality


closeness = calculate_closeness_centrality(road_map, cities_deleted_c)
print(closeness)
max_city = max(closeness, key=closeness.get)
print(
    f"The city with the highest closeness centrality is: {cities_deleted_c[max_city].name} ({max_city})"
)

betweenness = brandes_betweenness(road_map, cities_deleted_c)
print(betweenness)
max_city2 = max(betweenness, key=betweenness.get)
print(
    f"The city with the highest betweenness centrality is: {cities_deleted_c[max_city2].name} ({max_city2})"
)
