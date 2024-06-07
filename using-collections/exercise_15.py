# Without running the following code, what values will be printed by line 10?

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys() # dict_keys['Cat', 'Dog', 'Bird']
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# ['Cat', 'Bird', 'Snake'] x - dict_keys(['Cat', 'Bird', 'Snake']) - a dictionary view object
