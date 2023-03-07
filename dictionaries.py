#Dictionaries  have curly braces not squares braces. Dictinaries have key-value pairs
# dictionary = {'key':value, 'key':value, 'key':value, 'key':value}
# keys have to be a string but values can be numbers or strings.
# keys are used to access the values and don't have a specific order. 

states = {'NY':'New York', 'PA':'Pennsylvania', 'CA':'California'}
print(states['NY'])

# print(states['FL'])

people = ['Mattan', 'Chris']
# print(people[2])

print(type(states))
print(type(people))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)

# user = ['Raghav', 150, 9, 'Black', 'Brown']
user = {'name':'Raghav', 'height': 150, 'shoe-size': 9, 'hair':'Black', 'eyes':'Brown'}

print(user['name'])

# Dictionaries and Lists can be inside one other

animal_sounds = {
    "cat":["meow", "purr"],
    "dog":["Woof", "Bark"],
    "fox":[]
}

mattan = {'name':'Mattan', 'height': 150, 'shoe-size': 9, 'hair':'Black', 'eyes':'Brown'}
chris = {'name':'Chris', 'height': 68, 'shoe-size': 10, 'hair':'Brown', 'eyes':'Brown'}
sarah = {'name':'Sarah', 'height': 72, 'shoe-size': 8, 'hair':'Brown', 'eyes':'Brown'}

people = [mattan, chris, sarah]

print(people)

for person in people:
    print(person.get('height'))