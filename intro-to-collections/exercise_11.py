# Consider the data in the following table:

# Name	Country
# Alice	USA
# Francois	Canada
# Inti	Peru
# Monika	Germany
# Sanyu	Uganda
# Yoshitaka	Japan

# You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

my_data = [
    {'Alice': 'USA'},
    {'Francois': 'Canada'},
    {'Inti': 'Peru'},
    {'Monika': 'Germany'},
    {'Sanyu': 'Uganda'},
    {'Yoshitaka': 'Japan'},
]

print(my_data[2]['Inti'])

# Cleaner and more elegant solution

countries = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
}

print(countries['Inti'])
