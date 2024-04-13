# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = [] # empty list contains no numbers divisible by 5

print(all(remainders_5(numbers_1)))
print(remainders_5(numbers_1))
print(all(remainders_5(numbers_2)))
print(remainders_5(numbers_2))
print(all(remainders_5(numbers_3)))
print(remainders_5(numbers_3))
print(all(remainders_5(numbers_4)))
print(remainders_5(numbers_4))

# all(collection) => True if *all* elements are *truthy*, and False if *not* all are *truthy*
