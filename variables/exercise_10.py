# Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

# obj = 'ABcd'          # reassign's value to 'ABcd'
# obj.upper()           # neither doesn't mutate or reassign
# obj = obj.lower()     # reassign's value to 'abcd'
# print(len(obj))       # neither doesn't mutate or reassign
# obj = list(obj)       # reassign's value to ['a', 'b', 'c', 'd']
# obj.pop()             # neither removes the last value ['a', 'b', 'c'] [X - mutation]
# obj[2] = 'X'          # mutates the value at index 2 ['a', 'b', 'X']
# obj.sort()            # neither sorts the list, doesn't change it. [X - mutation] ['X', 'a', 'b']
# set(obj)              # neither creates a set doesn't change original value
# obj = tuple(obj)      # reassigns the value to a (X', 'a', 'b')
