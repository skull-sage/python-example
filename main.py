# to use from generator import comprehention, generator dir
# must have __init__.py

# MISCELLENEUS CONCEPTS
#import example_string
#import example_operator
#import example_exception

from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# add a title
plt.title("Nominal GDP")
# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()

# FUNCTION EXAMPLES

#import function_example.comprehension
#import function_example.generator
# import function_example.argument

#CLASS EXAMPLES

#import class_example.superman
#import class_example.overloading
