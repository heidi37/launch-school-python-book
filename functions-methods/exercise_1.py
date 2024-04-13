# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar' # initialization, foo is scope to the set_foo() definition

set_foo()
print(foo)

# This will throw an error because foo is a local variable and can't be accessed outside of the function.

# NameError: name 'foo' is not defined
