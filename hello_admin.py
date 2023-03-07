# 5-8 make a list of usernames and greet each user
admins = ['kuripanda', 'suhleek', 'liltury10', 'azulyte', 'changbinnie']
users = ['kuripanda', 'pokimane', 'suhleek', 'azulyte', 'changbinnie']
for user in users:
	if user in admins:
		print('Hello admin, would you like to see a status report?')
	else:
		print(f'Hello {user}, thank you for logging in again!')

# 5-9 clear admins list and print else statement saying we need users
print('\nExercise 5-9')
admins.clear()
if admins:
	for admin in admins:
		print(f'Hello {admin}!')
else:
	print('We need to find some users!')


#5-10 create a program that makes sure each username is unique
print('\nExercise 5-10')
current_users = ['kuri', 'suhleek', 'tury', 'haannaaah', 'azu']
new_users = ['kuri22', 'Suhleek', 'liltury', 'haannaaah', 'azulyte']
for user in new_users:
	if user.lower() in current_users:
		print(f'{user} is already taken.  Please create new username.')
	else:
		print(f'{user} is available!')

#5-11 store 1-9 in a list and loop to make ordinal numbers
print('\nExercise 5-11')
numbers = list(range(1,10))
for num in numbers:
	if num == 1:
		print(f'{num}st')
	elif num == 2:
		print(f'{num}nd')
	elif num == 3:
		print(f'{num}rd')
	else:
		print(f'{num}th')
