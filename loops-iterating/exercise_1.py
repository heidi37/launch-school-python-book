# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# This code causes an infinite loop because counter is never incremented within the body of the loop so it will remain less than 5 and continue running infinitely
