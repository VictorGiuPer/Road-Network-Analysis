"""
This code block defines and executes a 
function that performs the following tasks:

1. Creates a list of country codes corresponding 
   to each city in cities_dict1.

2. Counts how many times each country code appears, 
   effectively tallying the number of cities per country.

3. Sorts the country codes by the number of 
   associated cities in descending order.

4. Replaces the country codes with the actual 
   country names from countries_dict1.

5. This operation is useful for understanding the distribution
   of cities across countries within the provided datasets.
"""

# Import data
from initialization import cities_dict, countries_dict, roads_dict


def match_city_country(cities_dict1, countries_dict1):
    # Create an empty list to store country codes
    country_list = []
    # Iterate over each city in cities_dict1
    for city in cities_dict1:
        try:
            # Attempt to get the country code and add it to the country_list
            country_code = cities_dict1[city].country_n
            country_list.append(country_code)
        except:
            raise KeyError(f"City '{city}'", "does not have a country_n key.")

    # Initialize a counter dictionary to count occurrences of country codes
    counter = {}
    for country_code in range(len(countries_dict1)):
        count = country_list.count(country_code)
        counter[country_code] = count

    # Sort the counter dictionary by the count in descending order
    sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)

    # Convert the sorted items back into a dictionary
    sorted_counter = dict(sorted_items)
    # print(sorted_counter)

    # Convert the sorted items back into a dictionary
    ordered_country_list = []
    for country_code in sorted_counter:
        try:
            # Add the country name to the ordered list
            ordered_country_list.append(country_code)
        except:
            # Raise an error if the country name is not found
            raise ValueError(
                f"Country code '{country_code}'", "does not have a c_name key."
            )

    for country in ordered_country_list:
        ordered_country_list[ordered_country_list.index(country)] = countries_dict1[
            country
        ].c_name

    # print(f"Ordered list: \n{ordered_country_list}")


output = match_city_country(cities_dict, countries_dict)


"""
Time complexity analysis:


Creating the country_list:

The first loop iterates over all cities to create a list of country codes.
This loop runs in O(m), where m is the total number of cities.

------

Counting the cities per country:

The second loop iterates over the range of countries_dict1, which contains n countries.
Inside this loop, the count method is called, which runs in O(m) for each country, as 
it has to scan the entire country_list.

The overall complexity for this part is O(n⋅m), 
which can be significant if both n and m are large.

------

Sorting the counts:
The sorted function is used to sort the countries based on the count of cities.
Assuming a standard sorting algorithm, which has a worst-case complexity 
of O(nlogn), the complexity here is based on the number of countries, n.

So, for sorting, the complexity is O(nlogn).

------

Creating the ordered_country_list:

This involves iterating over the sorted_counter dictionary and then 
replacing the country codes with country names.

The replacement operation uses index, which is O(n) for each lookup 
since it scans the list to find the index.
The overall complexity for creating and populating ordered_country_list is O(n^2),
because for each of the n countries, an O(n) index lookup is performed. 

Overall Theoretical Runtime Complexity:

The dominant term in the overall complexity is the O(n⋅m) from the counting step, 
followed by the O(n^2) from creating the ordered_country_list. 
Therefore, the overall complexity is O(n⋅m+n^2), which simplifies to O(n⋅(m+n)) 
or just O(n⋅m) if we assume m is much larger than n, which is the case since 
there are more cities than countries.

------

In Summary:
For n as the total number of countries, the relevant complexities 
are O(n⋅m) for counting and O(nlogn) for sorting.

For m as the total number of cities, the initial loop that 
creates the country_list has a complexity of O(m).
"""
