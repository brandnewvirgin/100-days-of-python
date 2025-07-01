# Data types

# String

print("Hello" [4])

print("123" + "456")

#Integer

print(123 + 456)

print(123_456_789 + 987_654_321)

#float

print(3.14159 + 2.71842)

#Boolean

True
False
print(True + True)  # 1 + 1 = 2


# #call out the strings
# two_digit_number = input()

# #convert the strings to integers

# first_digit = int(two_digit_number [0])
# second_digit = int(two_digit_number [1])

# #print the sum of the two digits

# print(first_digit + second_digit)

print(1 + 5)  # Addition
print(8 - 2)  # Subtraction
print(3 * 2)  # Multiplication
print(12 / 2)  # Division
print(7 ** 3)  # Exponentiation
print(10 // 3)  # Floor Division

# PEMDASLR in python for calculations:
# Parentheses: ()
# Exponents: **
# Multiplication: *
# Division: /
# Addition: +
# Subtraction: -
#code is executed from left to right

# print(3 * 3 + 3 / 3 - 3)  # 9 + 1 - 3 = 7
# print(3 * (3 + 3) / 3 - 3)  # 3 * 6 / 3 - 3 = 6 - 3 = 3

# #input height in meters
# height = input()
# #input weight in kg
# weight = input()
# #convert height to float
# height = float(height)
# #convert weight to int
# weight = int(weight)
# #calculate BMI
# bmi = weight / (height ** 2)
# #print BMI
# print("Your BMI is: " + str(bmi))

# weight = int(input())
# height = float(input())
# bmi = weight / (height ** 2)
# print("Your BMI is: " + str(bmi))

score = 7
height= 1.8
statement = True
#f-string
print(f"Your score is {score}, your height is {height} and your statement is {statement}")

# age = input()
# year = input()
# age_as_int = int(age)
# year_as_int = int(year)
# weeks_left = (90 - age_as_int) * 52
# print(f"You have {weeks_left} weeks left")

# print("Welcome to the tip calculator")
# print("How much was your total bill " + input())

# #The total bill is $150, to be slip between 5 people with a 12% tip.
# #Each person should pay (150 * 1.12) / 5 = 33.6
# # The total bill is $150, to be split between 5 people with a 12% tip.
# #Print the welcome statement
# print("Welcome to the tip calculator")
# #Input the total bill
# total_bill = float(input("What was the total bill? $"))
# #Calculate the tip amount based on the percentage
# tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
# #Input the number of people to split the bill
# people = int(input("How many people to split the bill? "))
# #Calculate the total amount each person should pay
# tip_amount = total_bill * (tip_percentage / 100)
# total_amount = total_bill + tip_amount
# each_person_amount = total_amount / people
# #Print the result
# print(f"Each person should pay: ${each_person_amount:.2f}")

#Print the welcome statement
print("Welcome to the tip calculator!")
#Input the total bill
bill = float(input("What is t the total bill? $ "))
#calculate the tip
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#convert the tip to a percentage
tip_percentage = tip / 100
#Input the number of people to split the bill
people = int(input("How many people to split the bill? "))
#calculate the total bill with tip
total_bill = bill + (bill * tip_percentage)
#Calculate the amount each person should pay
individual_bill = total_bill / people
##round the amount to 2 decimal places
final_individual_bill = round(individual_bill, 2)
#Format the amount to 2 decimal places
final_individual_bill = "{:.2f}".format(final_individual_bill) 
#Print the result
print(f"Each person should pay: ${final_individual_bill}")
#Alternative way to print the result
#print(f"Each person should pay: ${final_individual_bill:.2f}")