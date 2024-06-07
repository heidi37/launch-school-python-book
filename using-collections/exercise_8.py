# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 - searches index 21 to 34("for the fjords"), starting at 34 and returns the first f it finds which is "f" in fjords and its index in that slice is 8.
print(text.rfind('f', 21, 35))    # 29 - searches between 21 to 34 but it does not slice out those indices as a new array, it just searches between them. So it still finds the "f" in fjords but it returns the index of the orginal text # 29
