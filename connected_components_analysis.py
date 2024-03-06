"""
This code block defines and executes a function that:

Analyzes the road map to identify connected components

Keeps track of the countries involved in each component 
to ensure each country's cities are counted in only one component.

Utilizes depth-first search to explore the connectivity from each 
city that has not yet been visited, grouping connected cities into components.

Counts the number of cities in each component and the countries they belong to.

Prints the total number of connected components, the number of countries
 and cities in each component, and lists the countries included in each.

Outputs the total count of countries across all components.

The function is useful for understanding the structure and 
clustering of the road network after certain countries and 
their roads have been removed, which can have implications 
for regional planning and infrastructure development.
"""

from country_removal_simulation import cities_deleted_c, roads_deleted_c, road_map


def detect_components(road_map, cities_dict):

    visited = set()
    components = []
    country_components = []
    city_count_per_component = []

    def depth_first(city, current_component, countries_in_component):
        if city in visited:
            return False
        visited.add(city)
        country = cities_dict[city].country_n
        countries_in_component.add(country)
        current_component.add(city)
        for adjacent_city in road_map.get(city, []):
            depth_first(adjacent_city, current_component, countries_in_component)
        return True

    # Main loop that goes through all cities
    for city in road_map:
        if city not in visited:
            current_component = set()
            countries_in_component = set()
            if depth_first(city, current_component, countries_in_component):
                components.append(current_component)
                country_components.append(countries_in_component)
                city_count_per_component.append(len(current_component))

    # Now, print the results
    print(f" \nComponents found: {len(components)}")
    components_add = 0
    for i, comp in enumerate(components):
        print(f"Component {i+1}:")
        print(f" - Number of countries: {len(country_components[i])}")
        print(f" - Number of cities: {city_count_per_component[i]}")
        print(f" - Countries included: {''.join(str(country_components[i]))}")


# You would call this function like so, after you've removed the countries:
detect_components(road_map, cities_deleted_c)

"""
In the detect_components function, there are a few key parts to consider:

Depth-First Search (DFS): DFS has a runtime complexity of O(n + e) where
n is the number of cities (nodes) and e is the number of roads (edges).

Main Loop Over Cities: Since the algorithm ensures that each city is explored 
only once, this loop will run n times, where n is the total number of cities.

-----

Combining these two, the overall runtime complexity of the function is O(n + m), 
because we go through each city once, and for each city, we explore its adjacent 
cities via DFS. The m in the complexity accounts for the total number of road 
connections because, in the worst case, every city could be connected to every other city.
"""
