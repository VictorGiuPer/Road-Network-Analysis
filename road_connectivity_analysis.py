"""
This code block defines and executes a function that:

Categorizes roads from roads_dict2 as either "cross-country" 
(connecting cities in different countries) or "within-country" 
(connecting cities within the same country).

Counts the number of each type of road for every country in countries_dict2.

Sorts the countries by the number of within-country roads 
and cross-country roads in descending order.

Prints a report listing each country along with the count of 
within-country roads and cross-country roads associated with it.

The function is valuable for analyzing the connectivity of regions
within and across countries based on the road network data provided.
"""

from city_country_distribution import roads_dict, cities_dict, countries_dict


# Check cities of the roads -> check country code of cities -> if != cross country else country country -> attach value to dictionary| Country code is the country code of the city itself, which is the point a or b
import copy


def detemine_road_type(roads_dict2, cities_dict2, countries_dict2):

    # Initialize counters for cross-country and within-country roads
    cross = 0
    within = 0

    # Create copies of the countries_dict2 to track the counts
    cross_country = copy.deepcopy(countries_dict2)
    country_country = copy.deepcopy(countries_dict2)

    # Initialize counters for each country to 0
    for i in range(len(cross_country)):
        cross_country[i] = 0
        country_country[i] = 0

    # Iterate through each road in the roads dictionary
    for road in roads_dict2:
        # Iterate through each road in the roads dictionary
        country_code_a = cities_dict2[road.point_a].country_n
        country_code_b = cities_dict2[road.point_b].country_n

        # Check if the road is within the same country
        if country_code_a == country_code_b:
            country_country[country_code_a] += 1
            within += 1

        # If the road crosses into another country
        elif country_code_a != country_code_b:
            cross_country[country_code_a] += 1
            cross_country[country_code_b] += 1
            cross += 1

    # Sort the country-country and cross-country counters
    sorted_items_country = sorted(
        country_country.items(), key=lambda item: item[1], reverse=True
    )
    sorted_items_cross = sorted(
        cross_country.items(), key=lambda item: item[1], reverse=True
    )

    # Convert the sorted lists back into dictionaries
    cross_dict = dict(sorted_items_cross)
    country_dict = dict(sorted_items_country)

    # Print the road types for each country
    for k in country_dict:
        print(
            f"{countries_dict2[k].c_name}",
            f"| Within: {country_dict[k]} | Cross {cross_dict[k]}",
        )
    print(f"Total Within: {within}")
    print(f"Total Cross: {cross}")


detemine_road_type(roads_dict, cities_dict, countries_dict)


"""
Runtime analysis:

Initialization: 
O(1) since it involves setting up a fixed number of 
variables and does not depend on the size of the input.

Iterating through Roads: 
O(r) where r is the total number of roads, 
as the function checks each road once.

Sorting: 
O(nlogn), where n is the total number of countries, 
due to the sorting of countries based on road counts.

Overall Complexity:
The total runtime complexity is O(r)+O(nlogn) when considering 
both the number of roads and the number of countries.

------

In short, the function is linear with respect to the number 
of roads and log-linear with respect to the number of 
countries due to the sorting operation.

"""
