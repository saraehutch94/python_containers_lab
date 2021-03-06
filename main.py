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

# for loop --> print last two foods from foods tuple
# print(foods[4:6])

for food in foods[-2:]:
  print(food)

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

# Exercise 6:

cohort = []

for student, food in zip(students, foods):
  dictionary = {'student': student, 'fav_food': food}
  cohort.append(dictionary)
  
print(cohort)

# Exercise 7:

awesome_students = [f'{student} is awesome!' for student in students]

for student in awesome_students:
  print(student)

# Exercise 8:

foods_a = [f'{food}' for food in foods if ("a" in food)]

for food in foods_a:
  print(food)
