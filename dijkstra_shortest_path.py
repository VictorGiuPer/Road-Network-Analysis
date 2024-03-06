"""
This code block defines:

A DijkstraElement class to encapsulate a city node, its distance 
from the origin, and the prior node in the path.

A dijkstra function that implements Dijkstra's algorithm to find 
the shortest path between two cities in a road network.

The algorithm operates by maintaining a priority queue to explore 
the closest unvisited city first and updating distances to each 
city as shorter paths are found. It continues exploring until 
the destination is reached or no path exists.

Upon completion, the dijkstra function returns the shortest path 
from the origin to the destination city, including the cumulative 
distance at each step. The function also handles cases where a 
city is not in the road network or no path is possible.

The provided code then uses this function to find and print the 
shortest paths between two pairs of cities in the updated road map 
after certain countries have been removed. This is valuable for 
route planning and navigation within the modified road network.
"""

from country_removal_simulation import cities_deleted_c, roads_deleted_c, road_map


class DijkstraElement:
    def __init__(self, city, distance, prior=None):
        self._city = city
        self._distance = distance
        self._prior = prior

    @property
    def city(self):
        return self._city

    @property
    def distance(self):
        return self._distance

    @property
    def prior(self):
        return self._prior

    def __lt__(self, other):
        if isinstance(other, DijkstraElement):
            return self.distance < other.distance
        raise TypeError(f"Cannot compare {self.__class__} to {type(other)}")


# Dijkstra's shortest path implementation

import heapq


def dijkstra(map, origin, destination, cities_dict5):

    visited = {}
    priority_queue = []
    current = DijkstraElement(city=origin, distance=0)
    # loop is O(n), total O(n^2 log n)
    while True:
        if not current.city in visited:
            visited[current.city] = current
            if current.city == destination:
                break
            # loop is O(n), total O(n log n)
            if current.city not in cities_dict5:
                print(f"This city ({current.city})", "is not in the road network.")
            else:
                for neighbor in map[current.city]:
                    distance = current.distance + map[current.city][neighbor]
                    # heappush is O(log n)
                    heapq.heappush(
                        priority_queue,
                        DijkstraElement(
                            city=neighbor, distance=distance, prior=current
                        ),
                    )
        if len(priority_queue) == 0:
            print(f"No path from {origin} to {destination}")
            return []
        # heappop is O(log n)
        current = heapq.heappop(priority_queue)

    waypoint = current
    path = [(waypoint.city, waypoint.distance)]
    # loop is O(n)
    while waypoint.prior is not None:
        waypoint = waypoint.prior
        path.append((waypoint.city, waypoint.distance))

    return path[::-1]


# successful example
path_dijkstra = dijkstra(road_map, 742, 659, cities_deleted_c)

# failed example
path_dijkstra2 = dijkstra(road_map, 2, 68, cities_deleted_c)

if path_dijkstra:
    print(f"Path 1: {path_dijkstra}")
else:
    print("No path for these cities")

if path_dijkstra:
    print(f"Path 2: {path_dijkstra2}")
else:
    print("No path for these cities")
