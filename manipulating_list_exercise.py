# 3-4 create a guest list
guest_list = ['Soyeon', 'Poki', 'Jodi']
print(f'{guest_list[0]}, you are invited to dinner party!')
print(f'{guest_list[1]}, please join me for a dinner party!')
print(f'{guest_list[2]}, welcome to the dinner party!')

#3-5 Change the guest list
popped_guest = guest_list.pop(0)
print(f'{popped_guest}, can no longer attend the dinner party.')
guest_list.insert(0, 'Leslie')
print(f'{guest_list[0]}, you are invited to dinner party!')
print(f'{guest_list[1]}, please join me for a dinner party!')
print(f'{guest_list[2]}, welcome to the dinner party!')

# 3-6 inviting more guests
print('We have found a bigger table, so now more guests can attend.')
guest_list.insert(0, 'Sydney')
guest_list.insert(2, 'Lily')
guest_list.append('Rae')
print(f'{guest_list[0]}, you are invited to dinner party!')
print(f'{guest_list[1]}, please join me for a dinner party!')
print(f'{guest_list[2]}, welcome to the dinner party!')
print(f'{guest_list[3]}, you are invited to dinner party!')
print(f'{guest_list[4]}, please join me for a dinner party!')
print(f'{guest_list[5]}, welcome to the dinner party!')
print(len(guest_list))

# 3-7 shrinking the guest list
print('We can only invite two guests due to arrival time.')
pop_guest1 = guest_list.pop()
print(f'Sorry, {pop_guest1}, you are uninvited.')
pop_guest2 = guest_list.pop()
print(f'Sorry, {pop_guest2}, you are uninvited.')
pop_guest3 = guest_list.pop()
print(f'Sorry, {pop_guest3}, you are uninvited.')
pop_guest4 = guest_list.pop()
print(f'Sorry, {pop_guest4}, you are uninvited.')
print(f'{guest_list[0]} and {guest_list[1]} are still invited!')
del guest_list[0]
del guest_list[0]
print(guest_list)

