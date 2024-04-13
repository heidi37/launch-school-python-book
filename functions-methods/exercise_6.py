# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return # returns "none"
    print(words)

scream('Yipeee')

# nothing, the function returned(terminates the function) before the print statement
