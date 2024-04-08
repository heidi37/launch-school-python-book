# What will the following code do? Why?

# print(int('3.1415')) #3

# invalid literal for int() with base 10: '3.1415'
# python can't convert a string in a float format to an int, only to a float as below.

print(float('3.1415'))
