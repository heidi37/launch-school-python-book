def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

# function name: multiply - (defined on line 1, invoked on line 9)
# function parameters(left, right) - (defined on line 1, used on line 2)
# function name: get_num - (defined on line 4, invoked on lines 7 & 8)
# function parameters(prompt) - (defined on line 4 used on line 5)
# function name: float - (invoked on line 5)
# function parameters(input(prompt)) - (5) [X Argument not a parameter]
# function name: input - (invoked on line 5)
# function parameters(prompt) - (5) [X Argument not a parameter]
# function name: print - (10)
# function parameters(f'{first_number} * {second_number} = {product}') - (10) [X Argument not parameter]

# parameters are in function definitions not invocations
