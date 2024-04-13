# Take a look at this code snippet:
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why? It prints 'bar. We are printing foo outside of the function so it uses the value assigned to foo in the main scope.

# The variable created inside the function shadow the variable created outside of the function.
