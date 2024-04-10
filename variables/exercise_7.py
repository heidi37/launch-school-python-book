# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.
# Good Morning, Nina.
# Good Afternoon, Nina.
# Good Evening, Nina.

# This code will work but the variable should not be named "NAME", that implies that it is a constant and should not be re-assigned.
