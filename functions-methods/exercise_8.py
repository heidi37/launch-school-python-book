# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# error, too many parameters passed

# TypeError: foo() takes 2 positional arguments but 3 were given
