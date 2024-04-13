# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# It will throw a Type Error because it is missing 3 required position arguments
# [X only missing the first argument because the second tow are defaults]
