# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# Type Error missing a required positional argument for third
# [X - different type of error, SyntaxError because the third parameter must have a default value if the second parameter has one]
# SyntaxError: non-default argument follows default argument
