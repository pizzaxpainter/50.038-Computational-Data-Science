import numpy as np
import pandas as pd

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])

# Modify the cities table by adding a new boolean column that is True if and only if both of the following are True:
# The city is named after a saint.
# The city has an area greater than 50 square miles.
# Note: Boolean Series are combined using the bitwise, rather than the traditional boolean, operators.

cities['Saint'] = cities['City name'].apply(lambda name: name.startswith('San'))
cities['Large'] = cities['Area square miles'].apply(lambda area: area > 50)
cities['Saint & Large'] = cities['Saint'] & cities['Large']
print(cities)



