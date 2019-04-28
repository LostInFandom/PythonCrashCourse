motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print('_______________________________\n')

#Appending
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

print('_______________________________\n')
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yahmaha')
motorcycles.append('suzuki')

print(motorcycles)
print('_______________________________\n')

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
print('_______________________________\n')

#Removing things from lists using the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print('_______________________________\n')

#Removing things using the pop() method:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(2)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

print('_______________________________\n')
#Removing and item by value:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print('_______________________________\n')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

