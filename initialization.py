"""
This code block defines three classes
to model a simple geographic system:

"Country" represents a country, allowing 
for the retrieval and update of its name.

"City" represents a city, maintaining its name, 
associated country, and geographical coordinates, 
with functionality to retrieve and update these properties.

"Road" represents a road between two points (cities), 
encapsulating the starting point, ending point, 
and the distance between them, with functionality 
to retrieve and update these properties, ensuring 
that the distance is always a non-negative value
"""


class Country:
    def __init__(self, name):
        self.c_name = name

    @property
    def C_name(self):
        return self.name

    @C_name.setter
    def Country_n(self, value):
        self.c_name = value

    def __str__(self):
        return self.c_name

    def __repr__(self):
        return f'Country("{self.c_name}")'


class City:
    def __init__(self, name, country_n, coordinate_x_y):
        self.name = name
        self.country_n = country_n
        self.coordinate_x_y = coordinate_x_y

    @property
    def Name(self):
        return self.name

    @Name.setter
    def Name(self, value):
        self.name = value

    @property
    def Country_n(self):
        return self.country_n

    @Country_n.setter
    def Country_n(self, value):
        self.country_n = value

    @property
    def Coordinate_x_y(self):
        return self.coordinate_x_y

    @Coordinate_x_y.setter
    def Coordinate_x_y(self, value):
        self.coordinate_x_y = value


class Road:
    def __init__(self, point_a, point_b, distance):
        self.point_a = point_a
        self.point_b = point_b
        self.distance = distance

    @property
    def Point_a(self):
        return self.point_a

    @Point_a.setter
    def Point_a(self, value):
        self.point_a = value

    @property
    def Point_b(self):
        return self.point_b

    @Point_b.setter
    def set_point_b(self, value):
        self.point_b = value

    @property
    def Distance(self):
        return self.distance

    @Distance.setter
    def set_distance(self, value):
        if value >= 0:
            self.distance = value
        else:
            raise ValueError


"""
This code block reads data from three separate files. 
Each contain Python data structures in text form. 
It then evaluates them into Python dictionaries:

"cities_gps2.py" is read and its contents are 
evaluated to form a dictionary containing city 
names and their GPS coordinates.

"countries.py" is read and its contents are evaluated 
to form a dictionary containing country names.

"roads_europe.py" is read and its contents are 
evaluated to form a dictionary containing information
about roads connecting cities in Europe.

This code block is intended for "data initialization" 
to be used in further operations.
"""

with open("cities_gps.py", "r", encoding="utf-8") as cities_data:
    cities_dict = eval(cities_data.read())
    # print(cities_dict)
with open(f"countries.py", "r", encoding="utf-8") as countries_data:
    countries_dict = eval(countries_data.read())
    # print(countries_dict)

with open("roads_europe.py", "r", encoding="utf-8") as roads_data:
    roads_dict = eval(roads_data.read())
    # print(roads_dict)
