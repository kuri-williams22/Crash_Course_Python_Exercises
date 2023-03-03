# 4-3 use for loop to print numbers 1 to 20
for number in range(1,21):
	print(number)

# 4-4 make a list of numbers 1 to 1 mil and print
numbers = list(range(1,1_000_001))
print(numbers)

# 4-5 make a list of 1 to mil and use min and max func
numbers = list(range(1,1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6 use 3rd arg of range function to list odd nums 1-20
for odds in range(1,20,2):
	print(odds)

# 4-7 make a list of multiples of 3 and for loop to print
multiples_of_3 = list(range(3,30,3))
for num in multiples_of_3:
	print(num)

# 4-8 make a list of first 10 cubes and for loop to print each value
cubes = list(range(1,11))
for value in cubes:
	print(value**3)

# 4-9 use a list comprehension to generate list of first 10 cubes
cubed = [value**3 for value in range(1,11)]
print(cubed)