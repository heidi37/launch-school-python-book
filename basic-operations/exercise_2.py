# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# print(f'Ones place is {str(4936)[3]}.')
# print(f'Tens place is {str(4936)[2]}.')
# print(f'Hundreds place is {str(4936)[1]}.')
# print(f'Thousands place is {str(4936)[0]}.')


number = 4936
print(f'Ones place is {number % 10}.')
number = number // 10
print(f'Tens place is {number % 10}.')
number = number // 10
print(f'Hundreds place is {number % 10}.')
number = number // 10
print(f'Thousands place is {number}.')
