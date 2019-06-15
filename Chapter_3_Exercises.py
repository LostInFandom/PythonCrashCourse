#3-1. Names:
names = ['Ami', 'Christina', 'Tim', 'Elena', 'Bradley', 'Zon', 'Joshua']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print("________________________\n")

#3-2. Greetings:
names = ['Ami', 'Christina', 'Tim', 'Elena', 'Bradley', 'Zon', 'Joshua']
print(names[0] + " is...niftypants!")
print(names[1] + " is...awesomesauce!")
print(names[2] + " is...swankalicious!")
print(names[3] + " is...friendlydendly!")
print(names[4] + " is...radical!")
print(names[5] + " is...sassypancakes!")
print(names[6] + " is...chill!")
print("________________________\n")

#3-3. Your Own List
#Blegh. Cars.
cars = ['Honda', 'Mazda', 'Toyota', 'Aston Martin', 'Lambourghini']
print("If I could drive, I would like to own a " + cars[0] + ".")
print("If I could drive, I would like to own a " + cars[1] + ".")
print("If I could drive, I would like to own a " + cars[2] + ".")
print("If I could drive, I would like to own an " + cars[3] + ".")
print("If I could drive, I would like to own a " + cars[4] + ".")
print("________________________\n")

#3-4. Guest List
#If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that is at least three people of who you would like to invite to dinner.
#Then use your list to print a message to each person, inviting them to dinner.

guests = ['J.K. Rowling', 'Elton John', 'Marie Curie', 'Ada Lovelace', 'Isaac Newton', 'Thor']
print("Dear " + guests[0] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[1] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[2] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[3] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[4] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[5] + ": \nPlease attend my dinner party!\n")
print("________________________\n")

#3-5. Changing Guest List
guests = ['J.K. Rowling', 'Elton John', 'Marie Curie', 'Ada Lovelace', 'Isaac Newton', 'Thor']
cannot_attend = guests.pop(0)
print("Oh noooooo! " + cannot_attend + " can't make it. Well, Seanan McGuire is the better author anyway. What was I thinking?")
print(guests)

guests.append('Seanan McGuire')
print("Here is the new and improved guest list...")
print(guests)
print("Dear " + guests[0] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[1] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[2] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[3] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[4] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[5] + ": \nPlease attend my dinner party!\n")
print("________________________\n")

#3-6. More Guests!
print("We went on OfferUp and found a bigger dinner table! Let's invite MOAR PEOPLE!!!")
guests.insert(0, 'Albert Einstein')
guests.insert(3, 'Hermione Granger')
guests.append('Twilight Sparkle')
print(guests)
print("Dear " + guests[0] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[1] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[2] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[3] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[4] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[5] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[6] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[7] + ": \nPlease attend my dinner party!\n")
print("Dear " + guests[8] + ": \nPlease attend my dinner party!\n")

#3-7. Shrinking Guest List:
print("Two-day shipping costs HOW much?! Consarnit, OfferUp! ALright, looks like we can only invite two.")
print(guests)
rescind_invite = guests.pop(0)
print("Sorry, " + rescind_invite + ", but you are the weakest dinner guest. Good-bye!")
print(guests)
rescind_invite = guests.pop(0)
print("Sorry, " + rescind_invite + ", but you are the weakest dinner guest. Good-bye!")
print(guests)
rescind_invite = guests.pop(0)
print("Sorry, " + rescind_invite + ", but you are the weakest dinner guest. Good-bye!")
print(guests)
rescind_invite = guests.pop(0)
print("Sorry, " + rescind_invite + ", but you are the weakest dinner guest. Good-bye!")
print(guests)
rescind_invite = guests.pop(0)
print("Sorry, " + rescind_invite + ", but you are the weakest dinner guest. Good-bye!")
print(guests)
rescind_invite = guests.pop(0)
print("Sorry, " + rescind_invite + ", but you are the weakest dinner guest. Good-bye!")
print(guests)
rescind_invite = guests.pop(0)
print("Sorry, " + rescind_invite + ", but you are the weakest dinner guest. Good-bye!")
print(guests)

print("Luckily, " + guests[0] + " and " + guests[1] + " are of Superior Dinner Guest Quality.")
print(guests[0] + ", you are still invited! Please attend my dinner party. <3")
print(guests[1] + ", you are still invited! Please attend my dinner party. <3")
del guests[0]
del guests[0]
print(guests)

print("________________________\n")

#3-8. Seeing the World
# Think of at least FIVE places in the world you'd like to visit.
#Store locations in a list & print:
locations = ['ireland', 'scotland', 'greece', 'portugal', 'brazil']
print(locations)
#Apply the sorted function:
print(sorted(locations))
#Show that your list is still stored in its original order by printing it again
print(locations)
#Print your list in reverse using sorted Function
print(sorted(locations, reverse = True))
#Show that your list is still stored in its original order by printing 
#it again:
print(locations)
#Use reverse() Method to sort your list in reverse order & print to 
#show that the order has changed:
locations.reverse()
print(locations)
#Use reverse() Method to change the order of your list agian & print to 
#show the list back in its original order:
locations.reverse()
print(locations)
#Use sort() Method to change your list so it's stored in alphabetical 
#order & print the list to show that the order has been changed:
locations.sort()
print(locations)
#Use sort() Method to change your list so that it's stored in reverse
#alphabetical order & print the list to show that the order has changed:
locations.sort(reverse = True)
print(locations)

print("________________________\n")

#3-9 Dinner Guests
#Using one of the programs from Exercises 3-4 through 3-7, use len() 
#Function to print a message indicating the number of people attending 
#your dinner party:

guests = ['J.K. Rowling', 'Elton John', 'Marie Curie', 'Ada Lovelace', 'Isaac Newton', 'Thor']
print(len(guests))
print('There are ' + str(len(guests)) + ' guests attending my dinner party')

print("________________________\n")

#3-10. Every Function
#Think of something you could store in a list. Write a program that
#creates a list containing these items & then uses each Function 
#contained in this chapter at least once.

print("________________________\n")

#3-11. Intentional Error
#If you haven't received an index error in one of your programs yet, try
#to make one happen. Change an index in one of your programs to produce 
#an index error. MAKE SURE TO CORRECT THE ERROR BEFORE CLOSING THE 
#PROGRAM!!!
doggos = ['cocker spaniels', 'yorkies', 'golden retrievers', 
'labradoodles', 'westies', 'australian shepherds']
print(doggos[5])


