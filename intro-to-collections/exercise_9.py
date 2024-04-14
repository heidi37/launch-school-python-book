my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
print(another_list)
print(my_list[3]==another_list[3])

# Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal? Yes, they contain the same elements/values.
# Are the lists assigned to my_list and another_list the same object? No, they don't point to the same place in memory.
# Are the nested lists at index 3 of my_list and another_list equal? Yes, they contain the same elements and values.
# Are the nested lists at index 3 of my_list and another_list the same object? No [X - Yes. The two nested lists are the same object. The list constructor creates a shallow copy of the iterable passed as an argument. Shallow DON'T copies create new nested lists. Instead only a reference to the nested list gets copied.]
