# Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def describe_value(number):
    if number >= 0 and number <= 50:
        print("the value is between 0 and 50")
    elif number >= 51 and number <= 100:
        print("the number is between 51 and 100")
    elif number > 100:
        print("the value is greater than 100")
    else:
        print("the value is less than 0")

describe_value(-1)
