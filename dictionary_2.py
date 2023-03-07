# 6-7 Create 3 dictionaries representing diff ppl and store 3 dict in a list
person_1 = {'first_name': 'rae', 'last_name': 'theon', 'age': 27, 'city': 'seattle'}
person_2 = {'first_name': 'lily', 'last_name': 'sun', 'age': 21, 'city': 'portland'}
person_3 = {'first_name': 'jojo', 'last_name': 'circus', 'age': 30, 'city': 'jackson'}
people = [person_1, person_2, person_3]
for person in people:
	full_name = f"{person['first_name']} {person['last_name']}"
	age = person['age']
	location = person['city']
	print(f'{full_name.title()} \nAge: {age}\nCity: {location.title()}')
	print()

# 6-8 Create several dict of different pets and loop to print each pet and their info
pet_1 = {'name': 'kiwi', 'type': 'dog', 'owner': 'kuri'}
pet_2 = {'name': 'oli', 'type': 'cat', 'owner': 'khaleem'}
pet_3 = {'name': 'sunny', 'type': 'bird', 'owner': 'emi'}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
	print(f"Pet name: {pet['name'].title()} \nAnimal type: {pet['type'].title()} \nOwner: {pet['owner'].title()}")
	print()

# 6-9 create dict of fav places and assign some to each person
favorite_places = {
   'kuri': ['japan', 'greece', 'iceland'],
   'jamil': ['brazil', 'south korea', 'germany'],
   'arthur': ['jamaica', 'egypt', 'australia']
   }
for name, places in favorite_places.items():
	print(f'{name.title()} likes the following places ')
	for place in places:
		print(f'- {place.title()}')
	print()

# 6-10 modify code from 6-2 so people have more than 1 fav num
fav_number = {
    'kristina': [22, 7,], 
    'khalil': [5,30, 24], 
    'arturo': [4, 11], 
    'tommy': [29, 21], 
    'ash': [24, 8],
    }
for name, nums in fav_number.items():
	print(f'{name.title()} likes the following numbers:')
	for num in nums:
		print(num)
	print()

# 6-11 create dict about city facts and store in dict of cities
cities = {
    'tokyo': {
        'country': 'japan', 
        'population': '14 million', 
        'fact': 'originally known as Edo'
        },
    'santorini': {
        'country': 'greece', 
        'population': '13 thousand', 
        'fact': 'the island is on a volcanic rock'
        },
    'reykjavik': {
        'country': 'iceland', 
        'population': '123 thousand', 
        'fact': 'Reykjavik means "Smoky Bay"'
        }
    }
for city, city_info in cities.items():
	city_name = city.title()
	country = city_info['country'].title()
	population = city_info['population']
	fact = city_info['fact']
	print(f'{city_name}, {country} has a population of {population} people!')
	print(f'Fun fact: {fact}')
	print()