"""
This code block defines and executes a function that:

Runs both Dijkstra's algorithm and the A* algorithm 200 times 
with randomly chosen pairs of cities from the updated road network.

Measures and records the runtime of each algorithm for every execution, 
converting the time to milliseconds for precision.

Collects the length of the path found by each algorithm and the corresponding runtime.

Calculates the average runtime for paths of the same length.

Saves the path lengths and their respective average runtimes to a file named data_runtime.txt.

Plots the average runtimes against the path lengths for both algorithms, 
generating a graph that visualizes the performance comparison.

-----

The function and resulting plot provide an empirical analysis of the 
efficiency of the two algorithms, potentially revealing differences 
in performance based on the complexity of the pathfinding task. 
This analysis is particularly useful for selecting an appropriate 
algorithm for real-world applications where performance is critical.
"""

import random

from country_removal_simulation import cities_deleted_c, road_map
from Astar_pathfinding import astar, h_func
from dijkstra_shortest_path import dijkstra

import time
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def run_time_analysis():
    # initialize list to hold x and y values for plotting
    x_dijkstra = []
    y_dijkstra = []
    x_astar = []
    y_astar = []

    try:
        with open("data_runtime.txt", "r") as data:

            for i, line in enumerate(data, 1):
                if i == 1:
                    x_dijkstra = line.split(",")[:-1]
                elif i == 2:
                    y_dijkstra = line.split(",")[:-1]
                elif i == 3:
                    x_astar = line.split(",")[:-1]
                elif i == 4:
                    y_astar = line.split(",")[:-1]
    except:
        with open("data_runtime.txt", "w") as data:
            pass

    for rep in range(200):
        city1 = random.choice(list(cities_deleted_c.keys()))
        city2 = random.choice(list(cities_deleted_c.keys()))

        # print(f"\n{city1} --> {city2}")#\nDijkstra:")
        start_time_d = time.perf_counter()
        dijkstra_imp = dijkstra(road_map, city1, city2, cities_deleted_c)
        end_time_d = time.perf_counter()
        runtime_d = float((end_time_d - start_time_d) * 1000)  # Convert to milliseconds
        # print(runtime_d)
        len_dijk = int(len(dijkstra_imp))
        # print(len_dijk)

        if len_dijk >= 1:
            x_dijkstra.append(len_dijk)
            y_dijkstra.append(runtime_d)

        # print(f"\n{city1} --> {city2}")#\nA*:")
        start_time_a = time.perf_counter()
        astar_imp = astar(city1, city2, h_func, road_map, cities_deleted_c)
        end_time_a = time.perf_counter()
        runtime_a = float((end_time_a - start_time_a) * 1000)  # Convert to milliseconds
        # print(runtime_a)

        try:
            len_astar = int(len(astar_imp))
            # print(len_astar)
        except:
            len_astar = 0
            # print(len_astar)

        if len_astar >= 1:
            x_astar.append(len_astar)
            y_astar.append(runtime_a)

        def average_runtimes(x_values, y_values):
            unique_lengths = sorted(set(x_values))
            indices_per_length = {
                length: [i for i, x in enumerate(x_values) if x == length]
                for length in unique_lengths
            }
            return [
                sum(y_values[i] for i in indices) / len(indices)
                for length, indices in indices_per_length.items()
            ]

        x_dijkstra = [int(len_dijk) for len_dijk in x_dijkstra]
        x_astar = [int(len_astar) for len_astar in x_astar]
        y_dijkstra = [float(runtime_d) for runtime_d in y_dijkstra]
        y_astar = [float(runtime_a) for runtime_a in y_astar]

        y_dijkstra_averages = average_runtimes(x_dijkstra, y_dijkstra)
        y_astar_averages = average_runtimes(x_astar, y_astar)

        # Unique lengths are sorted
        x_dijkstra_unique = sorted(set(x_dijkstra))
        x_astar_unique = sorted(set(x_astar))

    if len_dijk and len_astar:
        with open("data_runtime.txt", "w") as data:
            for item in x_dijkstra:
                data.write(str(item) + ",")
            data.write("\n")
            for item in y_dijkstra:
                data.write(str(item) + ",")
            data.write("\n")
            for item in x_astar:
                data.write(str(item) + ",")
            data.write("\n")
            for item in y_astar:
                data.write(str(item) + ",")

        data.close()

    plt.plot(x_dijkstra_unique, y_dijkstra_averages, "o-", label="Dijkstra")
    plt.plot(x_astar_unique, y_astar_averages, "o-", label="A*")

    # Title and labels
    plt.title("Dijkstra vs. A*")
    plt.xlabel("Length of Path")
    plt.ylabel("Average Runtime in Milliseconds")

    # Configure x-axis and y-axis
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))

    # Display legend
    plt.legend()

    # Show plot
    plt.show()


# Run the analysis
run_time_analysis()
