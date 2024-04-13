# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# Hello [X - Python will produce an error if you don't pass enough arguments to correspond with the number of expected parameters]

# Can you pass fewer argument than there are defined parameters in Python? NO

# TypeError: foo() missing 1 required positional argument: 'qux'
