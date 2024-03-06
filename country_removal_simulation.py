"""
This code block defines and executes a function that interactively 
allows the user to remove a country from a dataset. 

The function performs the following actions:

Takes input: the name of the country they wish to remove.

Identifies and deletes the selected country from countries_dict3, 
its corresponding cities from cities_dict3, and any roads connected 
to those cities from roads_list3.

Continuously prompts the user to remove additional countries 
until they choose to stop.

------

After deletion:

Checks for cities that have become disconnected from the 
road network as a result of the removals.

Rebuilds the road map to reflect the current connections between 
the remaining cities, ignoring the deleted roads and cities.

Prints the list of disconnected cities and the final road map with the remaining connections.

Returns the updated lists of cities and roads, and the new road map.


This function is useful for simulating the effects of removing specific countries 
from a transportation network and assessing the impact on connectivity.

"""

import copy
from city_country_distribution import roads_dict, cities_dict, countries_dict


def remove_country(roads_list3, cities_dict3, countries_dict3):

    # print(len(roads_list3))

    # Create deep copies of the input dictionaries to avoid modifying originals
    countries_copy = copy.deepcopy(countries_dict3)
    cities_copy = copy.deepcopy(cities_dict3)
    roads_copy = copy.deepcopy(roads_list3)

    while True:
        choice_input = input("which country would you like to remove?: ")
        cities_to_delete = []
        roads_to_delete = []

        # Find the country code for the selected country
        for country in countries_copy:
            if countries_copy[country].c_name == choice_input:
                delete_code = country

                # Find cities within the selected country
                for city in cities_copy:
                    if cities_copy[city].country_n == delete_code:
                        cities_to_delete.append(city)

                        # Find roads connected to these cities
                        for road in roads_copy:
                            index = roads_copy.index(road)
                            if (road.point_a == city or road.point_b == city) and (
                                index not in roads_to_delete
                            ):
                                roads_to_delete.append(roads_copy.index(road))

                print(f"{choice_input} deleted.")
                break

        # print(cities_to_delete)
        # print(roads_to_delete)

        del countries_copy[delete_code]
        country_deleted_c = copy.deepcopy(countries_copy)

        # print(len(cities_deleted_c))

        for city_code in cities_to_delete:
            del cities_copy[city_code]

        cities_deleted_c = copy.deepcopy(cities_copy)

        # print(len(cities_deleted_c))

        roads_to_delete.sort(reverse=True)

        # print(roads_to_delete)

        # Delete the road at the specified index
        for road_index in roads_to_delete:
            # print(f"Deleting road at index {road_index}.")
            del roads_copy[road_index]

        roads_deleted_c = copy.deepcopy(roads_copy)

        # print(len(roads_deleted_c))

        choice2 = int(input("Delete another country? Yes [1] No [0]: "))
        if choice2 == 1:
            continue
        else:
            break

    # print(len(roads_deleted_c))

    # Rebuild the road map excluding the deleted countries and their roads
    not_connected = []
    for city in cities_deleted_c:
        connected = False
        for road in roads_deleted_c:
            if road.point_a == city or road.point_b == city:
                connected = True
                break
        if not connected:
            print(f"{city} ({cities_deleted_c[city].name}) is not connected.")
            not_connected.append(city)

    # Initialize the road map with empty dictionaries for each city
    road_map_generator = map(lambda city_code: (city_code, {}), cities_deleted_c.keys())
    road_map = dict(road_map_generator)

    # Populate the road map with the roads and distances using a for-loop
    for road in roads_deleted_c:
        city1 = road.point_a
        city2 = road.point_b
        distance = road.distance  # assuming each road has a 'distance' attribute

        road_map[city1][city2] = distance
        road_map[city2][city1] = distance

    # print(road_map)
    # print(cities_deleted_c)

    return cities_deleted_c, roads_deleted_c, road_map


cities_deleted_c, roads_deleted_c, road_map = remove_country(
    roads_dict, cities_dict, countries_dict
)
