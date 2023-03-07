# 5-1 write a series of conditional tests with a prediction print statement

name = 'khalil'
print('Is his name Khalil?  I predict True.')
print(name == 'khalil')
print(name.upper() == 'KHALIL')
print(name.title() == 'Khalil')
print(name.lower() == 'khalil')
print('Is his name Arturo?  I predict False.')
print(name == 'Arturo')
print(name == 'KHALIL')
print(name == 'Khalil')
print(name == 'KhAlIl')

# 5-2 create more conditional tests with a list
names = ['khalil', 'arturo', 'hannah', 'azu']
print('khalil' and 'azu' in names)
print('KHALIL' in names)
print('KHALIL'.lower() in names)
print('arturo' and 'hannah' in names)
print('arturo' and 'AZU' in names)
print('khalil' and 'khair' in names)
print('khair' not in names)
