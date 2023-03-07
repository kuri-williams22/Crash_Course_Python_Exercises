# 6-1 Use dictionary to store info about people
person = {'first_name': 'rae', 'last_name': 'theon', 'age': '27', 'city': 'washington' }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print()

# 6-2 Use a dictionary to store people's fav num
fav_number = {
    'kristina': 22, 
    'khalil': 5, 
    'arturo': 4, 
    'tommy': 29, 
    'ash': 24,
    }
person_1 = fav_number['kristina']
print(f"Kristina's favorite number is {person_1}.")
person_2 = fav_number['khalil']
print(f"Khalil's favorite number is {person_2}")
person_3 = fav_number['arturo']
print(f"Arturo's favorite number is {person_3}")
person_4 = fav_number['tommy']
print(f"Tommy's favorite number is {person_4}")
person_5 = fav_number['ash']
print(f"Ash's favorite number is {person_5}")
print()

# 6-3 Create a glossary using a dictionary to store some python terms
glossary = {
    'python': 'programming language',
    'print': 'displays the output',
    'variable': 'assigned name of a value',
    'min()': 'returns item with the lowest value',
    'max()': 'returns item with the highest value',
    }
print('~~ Python Glossary ~~')
for key, value in glossary.items():
	print(f'{key.title()}: {value}')
print()

# 6-5 create dictionary containing rivers and country and loop through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yellow river': 'china',
    }
print('Rivers'
	'\n----------')
for river in rivers:
	print(river.title())
print()
print('Countries'
	'\n-----------')
for country in rivers.values():
	print(country.title())
print()

# 6-6 use favorite_languages.py in book to loop through people who should take poll and thank those who already have
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    }
friends = ['khalil', 'jen', 'kota']
for friend in friends:
	print(f'Hi {friend}!')
	if friend in favorite_languages:
		print('Thank you for taking the poll!')
	else:
		print('Please take the poll!')
