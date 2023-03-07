# 5-3 create if statements to test a range of variables
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors: 
	print('Player earned 5 points!')
if 'red' in alien_colors:
	print('Player earned 10 points!')
# create an if statement that fails - no output
if 'black' in alien_colors:
	print('Player earned 20 points')

# 5-4 write an if-else chain for the aliens color list
alien = 'green'
if alien == 'green':
	print('Player earned 5 points!')
else:
	print('Player earned 10 points!')
alien_1 = 'red'
if alien_1 == 'green':
	print('Player earned 5 points!')
else:
	print('Player earned 10 points!')

# 5-5 turn if-else chain into if-elif-else chain
alien = 'green'
if alien == 'green':
	print('Player earned 5 points!')
elif alien == 'yellow':
	print('Player earned 10 points!')
else:
	print('Player earned 15 points!')
alien = 'yellow'
if alien == 'green':
	print('Player earned 5 points!')
elif alien == 'yellow':
	print('Player earned 10 points!')
else:
	print('Player earned 15 points!')
alien = 'red'
if alien == 'green':
	print('Player earned 5 points!')
elif alien == 'yellow':
	print('Player earned 10 points!')
else:
	print('Player earned 15 points!')

# 5-6 write if-elif-else chain that determines person stage of life
age = 28
if age < 2:
	print('This person is a baby')
elif age >= 2 and age < 4:
	print('This person is a toddler')
elif age >= 4 and age < 13:
	print('This person is a kid')
elif age >= 13 and age < 20:
	print('This person is a teenager')
elif age >= 20 and age < 65:
	print('This person is an adult')
else:
	print('This person is an elder')

# 5-7 make a list of fruit and write series of independent if statements
favorite_fruits = ['mango', 'cherry', 'grape']
if 'mango' in favorite_fruits:
	print('You like mangoes!')
if 'cherry' in favorite_fruits:
	print('You like cherries!')
if 'grape' in favorite_fruits:
	print('You like grapes!')
if 'pineapple' not in favorite_fruits:
	print('You do not like pineapples')
if 'cherry' and 'mango' in favorite_fruits:
	print('Cherries and mangoes are considered stone fruit!')
	