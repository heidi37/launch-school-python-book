# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).

my_old_tuple = (1,2,3,4,5)
my_new_tuple = tuple(reversed(my_old_tuple))[1:-1]
print((my_new_tuple))

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:0:-1]
print(result)
