"""
This code block defines and executes a function that:

Compares the results of the A* algorithm (path_astar) and 
Dijkstra's algorithm (path_dijkstra) to check if they yield equivalent 
shortest path distances** between the same pair of cities.

Executes this comparison 5 times with randomly selected pairs of cities from 
the cities_deleted_c dictionary to ensure a varied sample for testing.

Prints the cities involved in each test and the outcome, indicating 
whether both algorithms have found paths of equal length or different lengths.

This function is useful for verifying the consistency and correctness 
of the pathfinding algorithms implemented earlier. It is important to 
check that both algorithms provide the same result since they are both
designed to find the shortest path, albeit with different approaches
"""

import random

from country_removal_simulation import cities_deleted_c, roads_deleted_c, road_map
from Astar_pathfinding import astar, h_func
from dijkstra_shortest_path import dijkstra


def check_path_eq(path_astar, path_dijkstra):
    try:
        if path_astar[-1][-1] == path_dijkstra[-1][-1]:
            print(f"| A* == Dijkstra |", f"\nDistance: {path_astar[-1][-1]}")
        elif path_astar[-1][-1] != path_dijkstra[-1][-1]:
            print(
                f"| A* != Dijkstra |",
                f"\nDistance A*: {path_astar[-1][-1]}",
                f"Distance A*: {path_dijkstra[-1][-1]}",
            )
    except:
        pass


for rep in range(5):
    city1 = random.choice(list(cities_deleted_c.keys()))
    city2 = random.choice(list(cities_deleted_c.keys()))
    print(f"{city1} --> {city2}")
    check_path_eq(
        astar(city1, city2, h_func, road_map, cities_deleted_c),
        dijkstra(road_map, city1, city2, cities_deleted_c),
    )


# astar(516, 326, h_func, road_map, cities_deleted_c)
# dijkstra(road_map, 516, 326, cities_deleted_c)


"""

Dijkstra's Algorithm:
The worst-case time complexity is: O((V+E)logV), 
where V is the number of vertices and E is the number of edges.

The n in O(n) usually refers to the number of vertices V. 
However in this context (graph algorithms), it is more precise 
to describe complexity in terms of both V and E.

------

A* Algorithm
The theoretical worst-case time complexity is the same as Dijkstra's: O((V+E)logV), 
given that the heuristic function has a constant complexity.

Here again the n in O(n) refers to both V and E for more precision.

In practice, the efficiency of A* depends heavily on the quality 
of the heuristic function. A well-chosen heuristic can 
significantly reduce the number of explored nodes, often 
resulting in better performance compared to Dijkstra's. 

(Refer to )
"""
