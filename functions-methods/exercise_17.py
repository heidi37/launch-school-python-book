def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

# function names
# say() - defined on line one and invoked on line 7

# method names
# .upper() - invoked on line 7
# .lower() - invoked on line 7

# built-in functions
# print - invoked on line 2
# input - invoked on line 4 and 5
# max - invoked on line 7
