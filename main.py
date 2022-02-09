# Exercise 1:

# students list
students = ['Sara', 'Johaisi', 'Delimar', 'Javier', 'Ataur', 'Phil']

# second student
print(students[1])

# last student
print(students[-1])

# Exercise 2:

# foods tuple
foods = ('pizza', 'pasta', 'tostones', 'empanadas', 'gelato', 'sorbet')

# for loop --> iterate over foods tuple
for food in foods:
  print(f'{food} is a good foods')

# Exercise 3:

# print last two foods from foods tuple
print(foods[4:6])

# Exercise 4:

home_town = {
  'city': 'Braintree',
  'state': 'Massachusetts',
  'population': 35744
}

print(f'I was born in {home_town["city"]}, {home_town["state"]}, - population of {home_town["population"]}.')

# Exercise 5:

for key, value in home_town.items():
  print(f'{key} = {value}')

  