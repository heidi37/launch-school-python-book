# Identify all of the identifiers on each line of the following code.

def multiply(left, right): # multiply, left, right
    return left * right # left, right

def get_num(prompt): # get_num, prompt
    return float(input(prompt)) # prompt [X float] [X input]

first_number = get_num('Enter the first number: ') # first_number [X get_num]
second_number = get_num('Enter the second number: ') # second_number [X get_num]
product = multiply(first_number, second_number) # product, multiply, first_number, second_number
print(f'{first_number} * {second_number} = {product}') # first_number, second_number, product [X print]

# identifier is broader than variable, variable names, constant names, function names, function parameters, method names, method parameters, class and module names
