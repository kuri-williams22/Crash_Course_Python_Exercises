# 4-10 slice a list based on the index
dogs = ['kiwi', 'kozy', 'starr', 'storm', 'benjy', 'gigi', 'klutch']
print(f'The first three dogs in this list are: {dogs[0:3]}')
print(f'The middle three dogs in this list are: {dogs[2:5]}')
print(f'The last three dogs in this list are: {dogs[4:7]}')

# 4-11 use list from 4-1 to make a copy list
pizza_list = ['cheese', 'hawaiian', 'veggie']
friend_pizzas = pizza_list[:]
pizza_list.append('garlic chicken')
friend_pizzas.append('pepporoni')
print(pizza_list)
print(friend_pizzas)
