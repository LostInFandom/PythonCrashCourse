birds = ['fairy wrens', 'crows', 'pigeons', 'hawks', 'turkies', 'penguins']
print(birds)
print(birds[0])
print(birds[0].title())
print(birds[0].upper())
print(birds[0].lower())

print(birds[1])
print(birds[4])

#Accessing the last item in a list: use -1.
birds = ['fairy wrens', 'crows', 'pigeons', 'hawks', 'turkies', 'penguins']
print(birds[-1])
#...for the last item,
print(birds[-2])
#...for the second-to-last
print(birds[-3])
#...for the third-to-last, and so on.

#Concatenating strings using lists.
birds = ['fairy wren', 'crow', 'pigeon', 'hawk', 'turkey', 'penguin']
message = "The " + birds[0].lower() + " was the first bird species I learned about through Wikipedia."
print(message)
