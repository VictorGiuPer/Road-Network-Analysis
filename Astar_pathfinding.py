"""
This code block defines:

A Node class to represent a node (city) in the graph with properties
 for its current cost g, heuristic estimate h, and the evaluation function e.

An astar function that implements the A* search algorithm to find the 
shortest path between a start and goal city within a road map.

The A* search uses a heuristic to estimate the distance to the goal 
and prioritizes nodes with a lower estimated cost.

A manhattan_distance heuristic function, which calculates an estimated 
distance between two cities based on their coordinates.

A helper function add_to_open to manage the open set (priority queue) 
for the A* search.

The algorithm searches for the shortest path by exploring the most 
promising nodes first, based on the cost to reach the node plus the 
heuristic estimate from that node to the goal. It returns the path 
from the start to the goal city with the associated costs.

This approach is beneficial for efficient pathfinding in geographic 
information systems and route planning applications.
"""

import heapq
import math

from country_removal_simulation import cities_deleted_c, roads_deleted_c, road_map


class Node:
    # Initialize nodes
    def __init__(self, city, g, h, parent=None):
        self.city = city
        self.parent = parent
        self.g = g  # g(c): actual shortest path cost from start to node c
        self.h = h  # h(c): heuristic estimate from c to goal
        self.e = self.g + self.h  # e(c): evaluation function

    def __lt__(self, other):
        return self.e < other.e


def astar(start, goal, h_func, road_map, cities_dict4):
    if start not in cities_dict4 or (goal not in cities_dict4):
        return "The chosen city (cities) ar not in the road network"
    open_heap = []
    closed_set = set()
    start_node = Node(start, 0, h_func(start, goal, cities_dict4))
    heapq.heappush(open_heap, start_node)

    while open_heap:
        current_node = heapq.heappop(open_heap)
        closed_set.add(current_node.city)

        if current_node.city == goal:
            path = []
            while current_node is not None:
                path.append((current_node.city, current_node.g))
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        neighbors = road_map.get(current_node.city, {})
        for neighbor_city, road_distance in neighbors.items():
            if neighbor_city in closed_set:
                continue

            g = current_node.g + road_distance
            h = h_func(neighbor_city, goal, cities_dict4)
            neighbor_node = Node(neighbor_city, g, h, current_node)

            if add_to_open(open_heap, neighbor_node):
                heapq.heappush(open_heap, neighbor_node)

    print(f"There is no path from {start} to {goal}.")


def add_to_open(open_heap, neighbor_node):
    for node in open_heap:
        if neighbor_node.city == node.city and neighbor_node.g >= node.g:
            return False
    return True


def manhattan_distance(city, goal, cities_dict4):
    x1, y1 = (
        cities_dict4[city].coordinate_x_y[0],
        cities_dict4[city].coordinate_x_y[1],
    )
    x2, y2 = (
        cities_dict4[goal].coordinate_x_y[0],
        cities_dict4[goal].coordinate_x_y[1],
    )
    return abs(x1 - x2) + abs(y1 - y2)


# Define h_func to use the manhattan_distance
def h_func(city, goal, cities_dict4):
    return manhattan_distance(city, goal, cities_dict4)


# Example usage:

# Barcelona to Bari
path_astar = astar(43, 44, h_func, road_map, cities_deleted_c)
# Aachen to Bologna
path_astar2 = astar(2, 79, h_func, road_map, cities_deleted_c)
print(path_astar)
print(path_astar2)
