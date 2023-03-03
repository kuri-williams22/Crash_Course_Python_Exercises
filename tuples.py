# 4-13 create a tuple and replace two items
foods = ('fried rice', 'ramen', 'sushi', 'gyoza', 'yakisoba')
print('Original tuple')
for food in foods:
	print(food)
# foods[0] = 'coconut shrimp' # make sure python rejects change
foods = ('curry rice', 'somen', 'sushi', 'gyoza', 'yakisoba')
print('Modified tuple')
for food in foods:
	print(food)