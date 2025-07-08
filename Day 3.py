#if/else conditions

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in CM? "))
#
# if height >= 120:
#     print("You can ride the Rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride!")

#Comparison symbols
# > - Greater than
# < - less than
# >= - Greater than or equals to
# <= - Less than or equal toke
# == - Equals toke
# != - Not equal to

#Which number do you want to check
# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:  # Checks if remainder is 0
#     print("This is an even number")
#
# else: #Checks if the remaininder is 1
#     print("This is an odd number")

# #Nested if/else statement
# print("Welcome to the Rollercoaster")
# height = int(input("What is your height in CM? "))
# #Write the first condition
# if height >= 120:
#     print("You can ride the Rollercoaster")
#     age = int(input("Enter your age in years "))
#     #nest the second conition in the first condition
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     elif age <= 22:
#         print("Just kidding, you still have to pay $12")
#     elif age >= 18:
#         print("Yeah, you're still paying $12")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grew taller before you can ride")

# #BMI 2.0
# #Enter your height in meters
# height = float(input("Please enter your height in meters "))
# #Enter your weight in kilograms
# weight = int(input("Enter your weight in kilograms "))

# BMI = weight / (height **2)
# if BMI < 18.5:
#     print("Your BMI is " + str(BMI) + " and you are underweight")
# elif BMI <= 25:
#     print("Your BMI is " + str(BMI) + " and you are normal weight")
# elif BMI <= 30:
#     print("Your BMI is " + str(BMI) + " and you are slightly overweight")
# elif BMI <= 35:
#     print("Your BMI is " + str(BMI) + " and you are obese")
# elif BMI == 35:
#     print("Your BMI is " + str(BMI) + " and you are clinically obese")
# elif BMI >= 35:
#     print(("Your BMI is " + str(BMI) + " and you just a fat fuck"))
# else:
#     print("Your BMI is " + str(BMI) + " and you are normal weight")

# year = 1700 / 4
# print(year)
#
# leap year + int(input("Choose a year "))

#a leap year must have the following features
#Divisible by 4 without a remainder
#Divisible by 100 without a remainder
#Divisible by 400 without a remainder

# #Steps
# #Print the welcome statement
# print("Welcome to the leap year finder")
# year = int(input("Enter the year you want to check "))
#
# if year % 4 == 0:
#     print("This is a leap years")
# elif year % 100 == 0:
#     print("This is not a leap year")
# elif year  % 400 == 0:
#     print("This is a leap year")
# else:
#     print("This is not a leap year")

# print("Welcome to the leap year finder")
# year = int(input("Enter the year you want to check: "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("This is a leap year")
#         else:
#             print("This is not a leap year")
#     else:
#         print("This is a leap year")
# else:
#     print("This is not a leap year")

# #Multiple if statements
# print("Welcome to the Rollercoaster")
# height = int(input("What is your height in CM? "))
#
# #Write the first condition
# if height >= 120:
#     print("You can ride the Rollercoaster")
#     age = int(input("Enter your age in years "))
#     #nest the second conition in the first condition
#     if age < 12:
#         bill = 5
#         print("Children tickets $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets $7")
#     elif age <= 22:
#         bill = 12
#         print("Adult tickets are $12")
#     elif age >= 18:
#         bill = 12
#         print("anyone over 18 is paying $12")
#     else:
#         print("Please pay $12")
#     photo = input("Do you want a photo taken? Yes or No. ")
#     if photo == "Yes":
#         bill += 3 #bill = bill + 3
#
#         print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you have to grew taller before you can ride")

#Create a pizza order menu and price
#There are three sizes of pizza
#small pizza costs $15
#medium pizza costs $20
#large pizza costs $25
#adding pepperoni to small pizza costs $2
#adding pepperoni to medium or large pizza costs $3
#adding extra cheese to any pizza size costs $1

# #print welcome statement
# print("Welcome to Romeo's Pizza")
#
# size = input("What size of pizza do you want? S, M, or L? ")
# add_pepperoni = input("Do you want to add peppeproni to your pizza? Y or N ")
# extra_cheese = input("Do you want to add extra cheese to your pizza? Y or N ")
#
# S = int(15)
# M = int(20)
# L = int(25)
#
# if size == "S":
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             print("Your bill is 15")
#         else:
#             print("Your bill is $17")
#     else:
#         print("Your final bill is $18")

# #print welcome statement
# print("Welcome to Romeo's Pizza")
#
# #create an input for size
# size = input("What size of pizza do you want? S, M, or L? ")
# #create an input for added pepperoni
# add_pepperoni = input("Do you want to add peppeproni to your pizza? Y or N ")
# #create an input for extra cheese
# extra_cheese = input("Do you want to add extra cheese to your pizza? Y or N ")
# #create a variable for bill
# bill = 0
# #add if/else conditions forselecting pizza sizes
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is ${bill}")

# #Multiple if statements
# print("Welcome to the Rollercoaster")
# height = int(input("What is your height in CM? "))
#
# #Write the first condition
# if height >= 120:
#     print("You can ride the Rollercoaster")
#     age = int(input("Enter your age in years "))
#     #nest the second conition in the first condition
#     if age < 12:
#         bill = 5
#         print("Children tickets $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets $7")
#     elif age >= 45 and age <= 55:
#         bill = 0
#         print("Everything is going to be okay. Have a free ride on us")
#     elif age <= 22:
#         bill = 12
#         print("Adult tickets are $12")
#     else:
#         print("Please pay $12")
#     photo = input("Do you want a photo taken? Yes or No. ")
#     if photo == "Yes":
#         bill += 3 #bill = bill + 3
#
#         print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you have to grew taller before you can ride")

# #Love calculator
#
# #print welcome statement
# print("Welcome to the love calculator")
# name1 = input("Enter is your name ") #name of the first person
# name2 = input("Enter your partner's name ") #name of the second person
# #Give the word count a variable and set it to zero
# count = 0
# for T in name1:
#     print("Yes, the name contains letter T")

# # Love calculator
#
# # Print welcome statement
# print("Welcome to the love calculator")
#
# # Input names
# name1 = input("Enter your name: ")  # Name of the first person
# name2 = input("Enter your partner's name: ")  # Name of the second person
#
# # Combine both names into a single string
# combined_names = name1 + name2
#
# # Convert to lowercase for consistent counting
# lower_names = combined_names.lower()
#
# # Count letters in "TRUE"
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# # Count letters in "LOVE"
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# # Don't count 'e' again; it's already counted
# second_digit = l + o + v
#
# # Form final score
# score = int(str(first_digit) + str(second_digit))
# #convert the score back to an integer for easy comparison
# score = int(score)
# # Interpret and print result
# if (score < 10) or (score > 90):
#     print(f"Your score is {score}, you go together like mint and coke.")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}, I don't know what to tell you.")

# #Treasure Island Project
#
# #print welcome statement
#
# print("Welcome to Treasure Island\nYour mission is to find the treasure")
#
# #put all levels in lower case
# first_level = input("You arrive at a crossroad and have to choose between left and right.\nWhat is your choice? left or right? ").lower()
# second_level = input("Congratulations, you have chosen the right path and are now at a river.\nWill you swim across or wait to see if a boat will come? swim or wait? ").lower()
# third_level = input("Only a door seperates you from treasures beyond your wildest dreams.\nWhich door do you choose? red, blue or yellow? ").lower()
#
# if first_level == "left":
#     if second_level == "wait":
#         if third_level == "yellow":
#             print("Congratulations! You have found the treasure!")
#         elif third_level == "red":
#             print("Burned by fire.\nGame over")
#         elif third_level == "blue":
#             print("Eaten by Beasts.\nGame over")
#         else:
#             print("Game over")
#     elif second_level == "swim":
#         print("Attacked by Trout.\nGame over")
#     else:
#         print("Game over")
# elif first_level == "right":
#     print("Fall into a hole.\nGame over")
# else:
#     print("Game Over")
#
# #print the treasure box for effect
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')

#Treasure Island Project

#print welcome statement

print("Welcome to Treasure Island\nYour mission is to find the treasure")
#print the treasure box for effect
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

#put all levels in lower case
choice1 = input("You\'re at a crossroad.\nWhhere do you want to go? 'left' or 'right'? ").lower()

if choice1 == "left":
    #continue the game
    choice2 = input("You are at a lake with an island in the middle.\nType 'wait' to wait for a boat or 'swim' to swim across ").lower()
    if choice2 == "wait":
        #game will continue
        choice3 = input("You arrive at the island safely and there is a house with three doors.\nYellow, red and blue.\nWhich door will you choose? ").lower()
        if choice3 == "yellow":
            print("Hurray! You have found the treasure\nYou win")
        elif choice3 == "red":
            print("Ouch! Game Over\nYou were burned by fire")
        #end the game
        elif choice3 == "blue":
            print("Oooof! Game over\nYou were eaten by some hungry beasts")
        #end the game
        else:
            print("Game over\nYou failed")
    #end the game
    else:
        print("Game over\nYou were attacked by an angry Trout")
#end the game
else:
    print("Game over\nYou fell into a hole")