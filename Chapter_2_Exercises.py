#Here are the excercises listed in the 'Try It Yourself' section at the end of Chapter 2:
#See Python Crash Course (pages 28-29) for more details on each exercise.
#Written By: Kaila Stevenson
#Last Edited: 04/27/2019

#2-3. Personal Message
first_name = "Kaila"
print("Hello, " + first_name + ", would you like to learn some Python today?")
#It's getting a little crowded.
#Let's make some room!
print("________________________\n")

#2-4. Name Cases
dva_name = "Hana Song"
print(dva_name.upper())
print(dva_name.lower())
print(dva_name.title())
#It's getting a little crowded.
#Let's make some room!
print("________________________\n")

#2-5. Famous Quote I
print("Isaac Newton said, \"If I have seen further than others, it is by standing on the shoulders of giants.\"")

#2-6. Fmaous Quote II
famous_person = "Isaac Newton"
message = "said, \"If I have seen further than others, it is by standing on the shoulders of giants.\""
print(famous_person +" "+message)

#It's getting a little crowded.
#Let's make some room!
print("________________________\n")

#2-7. Stripping Names
full_name = " Kaila Stevenson "
print("\t" + full_name)
print("\n" + full_name)
#It's getting a little crowded.
#Let's make some room!
print("\n")

print("\n\t" + full_name)
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())

print("________________________\n")
#2-8. Number Eight
#Write addition, subtraction, multiplication, and division operations that each result in the number 8.
#Addition:
print(5+3)
#Subtraction:
print(100-92)
#Multiplication:
print(2*4)
#Division:
print(64/8)

print("________________________\n")
#2-9. Favorite Number:
#Store your favorite number in a variable. Then, using that variable, create a message that  reveals your favorite number.
favorite_number = 3
print("My favorite number is..." + str(favorite_number) +"!")

print("________________________\n")
#2-10. Adding Comments
#Add some Comments! :)

print("________________________\n")
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



